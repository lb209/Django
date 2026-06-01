from django.urls import path
from .views import register_user, login_user, create_order, dashboard_stats, api_home

urlpatterns = [
    path('', api_home, name='api_home'),
    path('register/', register_user, name='register_user'),          # 'api/' ہٹا دیا تاکہ فرنٹ اینڈ سے میچ ہو جائے
    path('login/', login_user, name='login_user'),                # 'api/' ہٹا دیا
    path('create-order/', create_order, name='create_order'),        # 'api/' ہٹا دیا
    path('dashboard-stats/', dashboard_stats, name='dashboard_stats'), # 'api/' ہٹا دیا
]