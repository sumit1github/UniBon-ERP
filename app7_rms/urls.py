from django.urls import path
from .views import RMSView, RMSOperationView, RMSFilterView
app_name = 'app7_rms'
urlpatterns = [
    path('admin_rms/rms_list_or_create',RMSView.as_view(),name="rms_list_or_create"),
    path('admin_rms/rms_operation/<str:m_id>/<str:operation>',RMSOperationView.as_view(),name="rms_operation"),
    path('admin_rms/rms_filter/<str:filter>',RMSFilterView.as_view(),name="rms_filter"),
]