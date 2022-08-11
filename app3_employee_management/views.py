from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .forms import EmployeeCreationForm, EmployeeDocumentForm
from .models import Employee, EmployeeDocuments
from app6_master.models import Designation
from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers.decorators import super_admin_only, login_required, employee_edit_permission
from helpers.pagination import paginate
import os
import json

app="app3_employee_management/" 
# Create your views here.


@method_decorator(login_required,name='dispatch')
@method_decorator(employee_edit_permission,name='dispatch')
class EmployeeAdd(View):
    form=EmployeeCreationForm
    model=Employee
    html=app+"employee_list.html"
    def get(self,request,*args,**kwargs):
        data_list=self.model.objects.all().order_by('-id')
        employee_list=paginate(request,data_list, 50)
        designation_list=Designation.objects.all()
        context={'form':self.form,'employee_list':employee_list,'designation_list':designation_list}
        return render(request,self.html,context)   

    def post(self,request,*args,**kwargs):
        form_data=self.form(request.POST,request.FILES)
        aadhaar_number=request.POST.get('addhar_number')
        if (self.model.objects.filter(addhar_number=aadhaar_number).exists())==True:
            messages.error(request,'Aadhaar number is already present in database')
            return redirect('app3_employee_management:add_employee') 

        if form_data.is_valid():
            data=form_data.save()

            # if request.POST.get('designation'):
            #     designation=Designation.objects.get(id=request.POST.get('designation'))
            #     data.designation=designation
            #     data.save()
            messages.success(request, "Employee Added successfully")
        else:
            messages.error(request,str(form_data.errors))

        return redirect('app3_employee_management:add_employee')                 


@method_decorator(login_required,name='dispatch')
@method_decorator(employee_edit_permission,name='dispatch')
class EmployeeEdit(View):
    form=EmployeeCreationForm
    model=Employee
    html=app+"edit_employee.html"
    def get(self,request,*args,**kwargs):
        u_id=kwargs.get('u_id')
        obj=self.model.objects.get(id=u_id)
        designation_list=Designation.objects.all()
        context={'form':self.form(instance=obj),'designation_list':designation_list,'obj':obj}
        return render(request,self.html,context)   

    def post(self,request,*args,**kwargs):
        u_id=kwargs.get('u_id')
        obj=self.model.objects.get(id=u_id)
        form_data=self.form(request.POST,request.FILES,instance=obj)

        if form_data.is_valid():
            data=form_data.save()
            
            # if request.POST.get('designation'):
            #     designation=Designation.objects.get(id=request.POST.get('designation'))
            #     data.designation=designation
            #     data.save()

            messages.success(request, "Employee Editted successfully")
        else:
            messages.error(request,str(form_data.errors))

        return redirect('app3_employee_management:edit_employee',(u_id))  

@method_decorator(login_required,name='dispatch')
@method_decorator(employee_edit_permission,name='dispatch')
class EmployeeDelete(View):
    form=EmployeeCreationForm
    model=Employee
    def get(self,request,*args,**kwargs):
        u_id=kwargs.get('u_id')
        obj=self.model.objects.get(id=u_id)

        if obj.profile_pic:
            if len(obj.profile_pic) > 0:
                os.remove(obj.profile_pic.path)
        obj.delete()
        messages.success(request,"Employee is deleted.")
        return redirect('app3_employee_management:add_employee') 

@method_decorator(login_required,name='dispatch')
@method_decorator(employee_edit_permission,name='dispatch')
class EmployeeDocumentsAdd(View):
    form=EmployeeDocumentForm
    model=EmployeeDocuments
    template=app+'documents.html'

    def get(self,request,*args,**kwargs):
        u_id=kwargs.get('u_id')
        employee=Employee.objects.get(id=u_id)
        all_docs=self.model.objects.filter(employee=employee)
        context={'doc_list':all_docs,'form':self.form,'u_id':u_id}
        return render(request,self.template,context)

    def post(self,request,*args,**kwargs):
        u_id=kwargs.get('u_id')
        employee=Employee.objects.get(id=u_id)

        form_data=self.form(request.POST,request.FILES)
        if form_data.is_valid():
            data=form_data.save()
            data.employee=employee
            data.save()
            messages.success(request,'Document is Added Succesfully')
        else:
            messages.error(request,str(form.errors))
        return redirect('app3_employee_management:employee_documents',u_id)
 

@method_decorator(login_required,name='dispatch')
@method_decorator(employee_edit_permission,name='dispatch')
class EmployeeDocumentsDelete(View):
    model=EmployeeDocuments
    def get(self,request,*args,**kwargs):
        d_id=kwargs.get('d_id')
        obj=EmployeeDocuments.objects.get(id=str(d_id))
        u_id=obj.employee.id
        if obj.file_data:
            if len(obj.file_data) > 0:
                os.remove(obj.file_data.path)
        obj.delete()
        messages.success(request,"Document is deleted.")
        return redirect('app3_employee_management:employee_documents',u_id) 