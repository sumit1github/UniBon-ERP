from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from .forms import DesignationCreationForm, UnitCreationForm, ItemCodeCreationForm, ItemCodeUpdateForm
from .models import Designation, Unit, ItemCode

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers.decorators import super_admin_only, login_required, product_edit_permission
from helpers.pagination import paginate
import os


app="app6_master/" 
# Create your views here.


@method_decorator(login_required,name='dispatch')
# Create your views here.
class DesignationView(View):
    model=Designation
    form=DesignationCreationForm
    template=app+"designation/designation.html"
    
    def get(self,request,*args,**kwargs):
        designation_list=self.model.objects.all().order_by('-id')
        designation_list=paginate(request, designation_list, 50)
        context={'designation_list':designation_list,'form':self.form}
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
        d_id=request.POST.get('d_id')

        #create new record
        if request.POST.get('operation')=="create_new":
            form_data=self.form(request.POST)
            if form_data.is_valid():
                data=form_data.save()
                message='New Designation is created'
                messages.success(request,message)
            else:
                messages.error(request,str(form_data.errors))
                
            return redirect ('app6_master:designation')
        
        elif (request.POST.get('operation'))=='update':
            data=self.model.objects.get(id=d_id)
            form=self.form(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request,"Designation Name is changed succesfully.")
            else:
                messages.error(request,str(form.errors))
            return redirect ('app6_master:designation')
        #delete designation
        elif (request.POST.get('operation'))=="delete":
            data=self.model.objects.get(id=id)
            data.delete()
            messages.success(request, 'Designation is deleted')
            return redirect ('app6_master:designation')
        

        else:
            messages.error(request, 'Instruction is missing')
            return redirect ('app6_master:designation')
        

@method_decorator(login_required,name='dispatch')
# Create your views here.
class UnitView(View):
    model=Unit
    form=UnitCreationForm
    template=app+"unit/unit_list.html"
    
    def get(self,request,*args,**kwargs):
        unit_list=self.model.objects.all().order_by('-id')
        unit_list=paginate(request, unit_list, 50)
        context={'unit_list':unit_list,'form':self.form}
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
       

        #create new record
        if request.POST.get('operation')=="create_new":
            form_data=self.form(request.POST)
            if form_data.is_valid():
                data=form_data.save()
                message='New Unit is created'
                messages.success(request,message)
            else:
                messages.error(request,str(form_data.errors))
                
            return redirect ('app6_master:unit')
        
        elif (request.POST.get('operation'))=='update':
            u_id=request.POST.get('u_id')
            print(u_id)
            data=self.model.objects.get(id=u_id)
            form=self.form(request.POST, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request,"Unit Name is changed succesfully.")
            else:
                messages.error(request,str(form.errors))
            return redirect ('app6_master:unit')
            
        #delete unit
        elif (request.POST.get('operation'))=="delete":
            data=self.model.objects.get(id=id)
            data.delete()
            messages.success(request, 'Unit is deleted')
            return redirect ('app6_master:unit')
        

        else:
            messages.error(request, 'Instruction is missing')
            return redirect ('app6_master:unit')


@method_decorator(login_required,name='dispatch')
# Create your views here.
class ItemCodeView(View):
    model=ItemCode
    form=ItemCodeCreationForm
    template=app+"item_code/item_code_list.html"
    
    def get(self,request,*args,**kwargs):
        item_code_list=self.model.objects.all().order_by('-id')
        item_code_list=paginate(request, item_code_list, 50)
        context={'item_code_list':item_code_list,'form':self.form}
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
       
        #create new record
        if request.POST.get('operation')=="create_new":
            form_data=self.form(request.POST)
            if form_data.is_valid():
                data=form_data.save()
                message='New Item Code is created'
                messages.success(request,message)
            else:
                messages.error(request,str(form_data.errors))
                
            return redirect ('app6_master:item_code')
                 

        else:
            messages.error(request, 'Instruction is missing')
            return redirect ('app6_master:item_code')


@method_decorator(login_required,name='dispatch')
# Create your views here.
class ItemCodeEditView(View):
    model=ItemCode
    form=ItemCodeUpdateForm
    template=app+"item_code/edit_code.html"

    def get(self,request,*args,**kwargs):
        i_id=kwargs.get('i_id')
        data=self.model.objects.get(id=i_id)
        context={'form':self.form(instance=data)}
        return render(request,self.template,context)
    
    def post(self,request,*args,**kwargs):          
        i_id=kwargs.get('i_id')
        data=self.model.objects.get(id=i_id)
        form=self.form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,"Item Code Data is changed succesfully.")
        else:
            messages.error(request,str(form.errors))
        return redirect ('app6_master:item_code')