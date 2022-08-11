
from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from .forms import ProductCreationForm
from .models import Product
from app6_master.models import ItemCode, Unit

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers.decorators import super_admin_only, login_required, product_edit_permission
from helpers.pagination import paginate
import os


app="app4_product/" 
# Create your views here.


@method_decorator(login_required,name='dispatch')
@method_decorator(product_edit_permission,name='dispatch')
# Create your views here.
class ProductCreationView(View):
    model=Product
    form=ProductCreationForm
    template=app+"product_list.html"
    
    def get(self,request,*args,**kwargs):
        product_list=self.model.objects.all().order_by('-id')
        product_list=paginate(request, product_list, 10)
        context={'product_list':product_list,'form':self.form}
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
        form_data=self.form(request.POST)
        if form_data.is_valid():
            data=form_data.save()
            message=data.name +' with code ' +'is crated'
            messages.success(request,message)
        else:
            messages.error(request,str(form_data.errors))
            
        return redirect ('app4_product:product_list_create')


@method_decorator(login_required,name='dispatch')
@method_decorator(product_edit_permission,name='dispatch')
class ProductUpdateView(View):
    model=Product
    form=ProductCreationForm
    template=app+"edit_product.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get('p_id')
        product=self.model.objects.get(id=id)
        form=self.form(instance=product)
        context={'form':form}
        return render(request,self.template,context)
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get('p_id')
        product=self.model.objects.get(id=id)
        ser = self.form(request.POST,request.FILES,instance=product)
        if ser.is_valid():
            ser.save()
            messages.success(request, "Product is updated")
            return redirect('app4_product:product_list_create')
        else:
            messages.error(request, str(ser.errors))
            return redirect('app4_product:product_list_create')


@method_decorator(login_required,name='dispatch')
@method_decorator(product_edit_permission,name='dispatch')
class ProductdelteView(View):
    model=Product
    template=app+"edit_product.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get('p_id')
        product=self.model.objects.get(id=id)
        product.delete()
        messages.success(request, "Product is deleted.")
        return redirect('app4_product:product_list_create')

@method_decorator(login_required,name='dispatch')
@method_decorator(product_edit_permission,name='dispatch')
class ProductsearchView(View):
    model=Product
    form=ProductCreationForm
    template=app+"product_list.html"
    def post(self,request,*args,**kwargs):
        query=request.POST.get('query')
        product1=[]
        product2=[]
        product3=[]
        try:
            id=int(query)
            product=self.model.objects.filter(id=id).first()
            context={'product_list':product,'form':self.form}
            return render(request, self.tempalte, context)
        except:
            product1=self.model.objects.filter(id=id).first()
            product.delete()
            messages.success(request, "Product is deleted.")
        return redirect('app4_product:product_list_create')
        
    #     eid = int(eid)
    #     emp2 = Employee.objects.filter(id=eid)
    #     context = {"product_list": emp2}
    #     return render(request, "emp_template/emp_list.html", context)
    # except ValueError:
    #     pass
    # emp3 = Employee.objects.filter(Aadhaar_NO__icontains=eid)
    # emp = emp1 | emp3
    # context = {"product_list": emp}