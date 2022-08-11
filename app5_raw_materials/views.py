
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from .forms import *
from .models import *

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers.decorators import super_admin_only, login_required, product_edit_permission
from helpers.pagination import paginate
import os


app="app5_raw_materials/" 
# Create your views here.


# @method_decorator(login_required,name='dispatch')
# @method_decorator(product_edit_permission,name='dispatch')
# # Create your views here.
# class ProductCreationView(View):
#     model=Product
#     form=ProductCreationForm
#     template=app+"product/product_list.html"
    
#     def get(self,request,*args,**kwargs):
#         product_list=self.model.objects.all().order_by('-id')
#         product_list=paginate(request, product_list, 10)
#         context={'product_list':product_list,'form':self.form}
#         return render(request,self.template,context)

#     def post(self,request,*args,**kwargs):
#         form_data=self.form(request.POST)
#         if form_data.is_valid():
#             data=form_data.save()
#             message=data.name +' with code '+ data.sku_start+str(data.id) +' is crated'
#             messages.success(request,message)
#         else:
#             messages.error(request,str(form_data.errors))
            
#         return redirect ('app4_product:product_list_create')


# @method_decorator(login_required,name='dispatch')
# @method_decorator(product_edit_permission,name='dispatch')
# class ProductUpdateView(View):
#     model=Product
#     form=ProductCreationForm
#     template=app+"product/edit_product.html"
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('p_id')
#         product=self.model.objects.get(id=id)
#         form=self.form(instance=product)
#         context={'form':form}
#         return render(request,self.template,context)
    
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get('p_id')
#         product=self.model.objects.get(id=id)
#         ser = self.form(request.POST,request.FILES,instance=product)
#         if ser.is_valid():
#             ser.save()
#             messages.success(request, "Product is updated")
#             return redirect('app4_product:product_list_create')
#         else:
#             messages.error(request, str(ser.errors))
#             return redirect('app4_product:product_list_create')


# @method_decorator(login_required,name='dispatch')
# @method_decorator(product_edit_permission,name='dispatch')
# class ProductdelteView(View):
#     model=Product
#     template=app+"product/edit_product.html"
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get('p_id')
#         product=self.model.objects.get(id=id)
#         product.delete()
#         messages.success(request, "Product is deleted.")
#         return redirect('app4_product:product_list_create')