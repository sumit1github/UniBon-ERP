from django.db import models
from django.contrib import admin
from app6_master.models import Designation
# Create your models here.
class Employee(models.Model):
 
    name=models.CharField(max_length=255,null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    contact1=models.CharField(max_length=255,null=True,blank=True)
    contact2=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)

    profile_pic=models.ImageField(upload_to="employee_images/",null=True,blank=True)

    date_of_joining=models.CharField(max_length=255,null=True,blank=True)
    date_of_leaving=models.CharField(max_length=255,null=True,blank=True)

    addhar_number=models.CharField(max_length=255,null=True,blank=True)
    driving_lisence=models.CharField(max_length=255,null=True,blank=True)
    pan_card=models.CharField(max_length=255,null=True,blank=True)

    bank_ac_number=models.CharField(max_length=255,null=True,blank=True)
    ifsc_code=models.CharField(max_length=255,null=True,blank=True)

    working_hour=models.CharField(max_length=255,null=True,blank=True)
    basic_salary=models.FloatField(default=0.0)
    extra_money=models.FloatField(default=0.0)
    advance=models.FloatField(default=0.0)
    designation=models.ForeignKey(Designation,on_delete=models.SET_NULL,null=True,blank=True)
    locker_number=models.CharField(max_length=255,null=True,blank=True)

    is_active=models.BooleanField(default=True)
    extra_info=models.TextField(null=True,blank=True)

admin.site.register(Employee)

class EmployeeDocuments(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    file_data=models.FileField(upload_to='employee_documents/',null=True,blank=True)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, null=True,blank=True)

admin.site.register(EmployeeDocuments)