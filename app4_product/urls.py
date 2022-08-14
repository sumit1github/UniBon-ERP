from django.urls import path
from .views import ProductCreationView, ProductUpdateView, ProductdelteView, ProductsearchView
app_name = 'app4_product'
urlpatterns = [
   path('product/product_list_create', ProductCreationView.as_view(), name="product_list_create"),
   path('product/product_update/<str:p_id>', ProductUpdateView.as_view(), name="product_update"),
   path('product/product_delete/<str:p_id>', ProductdelteView.as_view(), name="product_delete"),
   path('product/search_product',ProductsearchView.as_view(),name="search_product"),
] 