from django.urls import path
from .views import AdminDashboard
app_name = 'app2_admin_dashboard'
urlpatterns = [
    path('',AdminDashboard.as_view(),name='admin_dashboard_home')
]