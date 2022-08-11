from django.urls import path
from .views import DesignationView, UnitView, ItemCodeView, ItemCodeEditView
app_name = 'app6_master'
urlpatterns = [
   path('master/designation',DesignationView.as_view(),name="designation"),
   path('master/unit',UnitView.as_view(),name="unit"),
   path('master/item_code',ItemCodeView.as_view(),name="item_code"),
   path('master/item_code_edit/<str:i_id>',ItemCodeEditView.as_view(),name="item_code_edit"),
] 