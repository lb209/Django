import re
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Sum
from django.http import JsonResponse
from .models import Order

@csrf_exempt
@api_view(['POST'])
@authentication_classes([])  # DRF کا سیشن سیکیورٹی چیک بائی پاس کرنے کے لیے
@permission_classes([])      # اوپن اینڈ پوائنٹ بنانے کے لیے
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({"success": False, "error": "All fields are required"})

    if User.objects.filter(username=username).exists():
        return Response({"success": False, "error": "Username already exists"})

    if User.objects.filter(email=email).exists():
        return Response({"success": False, "error": "Email already exists"})

    if len(password) < 8:
        return Response({"success": False, "error": "Password must be at least 8 characters"})

    if not re.search(r"[0-9]", password):
        return Response({"success": False, "error": "Password must contain a number"})

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>/]", password):
        return Response({"success": False, "error": "Password must contain a special character"})

    User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response({
        "success": True,
        "message": "Signup successfully!"
    })


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])  # CSRF Forbidden ایرر کو حل کرنے کے لیے سب سے اہم لائن
@permission_classes([])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({
            "success": False,
            "error": "All fields are required"
        })

    try:
        user_obj = User.objects.get(email=email)
        actual_username = user_obj.username
    except User.DoesNotExist:
        return Response({
            "success": False,
            "error": "Email not found"
        })

    user = authenticate(
        username=actual_username,
        password=password
    )

    if user:
        return Response({
            "success": True,
            "username": user.username,
            "message": "Login successful"
        })

    return Response({
        "success": False,
        "error": "Invalid Email or Password"
    })


@csrf_exempt
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_order(request):
    card_number = request.data.get('card_number')
    total_price = request.data.get('total_price')

    if not card_number or not total_price:
        return Response({
            "success": False,
            "error": "Card number and total price are required"
        })

    if not re.match(r"^\d{11}$", str(card_number)):
        return Response({
            "success": False,
            "error": "Card number must be exactly 11 digits"
        })

    Order.objects.create(
        card_number=card_number,
        total_price=total_price,
        status='Completed'
    )

    return Response({
        "success": True,
        "message": "Order placed successfully!"
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def dashboard_stats(request):
    total_orders = Order.objects.count()

    revenue_sum = (
        Order.objects.aggregate(
            Sum('total_price')
        )['total_price__sum'] or 0
    )

    return Response({
        "total_orders": total_orders,
        "raw_revenue": float(revenue_sum)
    })


def api_home(request):
    return JsonResponse({
        "message": "Welcome to Foodie API Backend!",
        "status": "Running",
        "available_endpoints": [
            "/register/",
            "/login/",
            "/create-order/",
            "/dashboard-stats/"
        ]
    })