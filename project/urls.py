from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1_authentication.urls')),
    path('auth/',include('app1_authentication.urls')),
    path('user_manage/',include('app1_authentication.urls')),
    path('admin_dashboard/',include('app2_admin_dashboard.urls')),
    path('employee_manage/',include('app3_employee_management.urls')),
    path('product_manage/',include('app4_product.urls')),
    path('raw_materials/',include('app5_raw_materials.urls')),
    path('master_data/',include('app6_master.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
