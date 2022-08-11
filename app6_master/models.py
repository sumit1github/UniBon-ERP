from django.db import models
from django.contrib import admin
# Create your models here.
class Designation(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.name
admin.site.register(Designation)

class Unit(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return self.name
admin.site.register(Unit)

class ItemCode(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    code_start_with=models.CharField(max_length=255,null=True,blank=True)
    def __str__(self):
        return str(self.name+"-"+self.code_start_with)
admin.site.register(ItemCode)