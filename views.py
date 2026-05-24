from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from myproject.forms import RegistrationForm
from .models import Student


# ---------------- HOME ----------------
def home(request):
    return render(request, "home/home.html")


# ---------------- REGISTER ----------------
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "Please fill all fields")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        if len(password) < 4:
            messages.error(request, "Password too short")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('login')

    return render(request, 'home/register.html')


# ---------------- LOGIN ----------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('read')   # FIX: render نہیں، redirect
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("login")

    return render(request, 'home/login.html')


# ---------------- LOGOUT ----------------
def logout_user(request):
    logout(request)
    return redirect("login")


# ---------------- READ ----------------
def read_student(request):
    student = Student.objects.all()
    form = RegistrationForm()

    return render(request, 'home/read.html', {
        'students': student,
        'form': form,
    })


# ---------------- CREATE ----------------
def create_student(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            Student.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                city=form.cleaned_data['city'],
                image=form.cleaned_data['image']
            )

    return redirect('read')


# ---------------- UPDATE ----------------
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)

        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.age = form.cleaned_data['age']
            student.city = form.cleaned_data['city']

            if form.cleaned_data.get('image'):
                student.image = form.cleaned_data['image']

            student.save()

    return redirect('read')


# ---------------- DELETE ----------------
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('read')



def search_student(request):
    search= request.GET.get('search')
    sort=request.GET.get('sort')

    students=Student.objects.all()

    if search:
        students= Student.objects.filter( name__contains=search)

        #sort
    if sort == 'asc':
        students=students.order_by('name')

    elif sort == 'desc':
        students = students.order_by('-name')

    elif sort == 'age_low':
        students = students.order_by('age')

    elif sort == 'age_high':
        students = students.order_by('-age')


    form = RegistrationForm()

    return render(request, 'home/read.html', {
        'students': students,
        'form': form,
    })