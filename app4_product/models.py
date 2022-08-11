from django.db import models
from app6_master.models import Unit, ItemCode
from django.contrib import admin
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)

    unit=models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True)
    Item_code=models.ForeignKey(ItemCode, on_delete=models.SET_NULL, blank=True, null=True)

    remarks=models.TextField(null=True,blank=True)
    def __str__(self):
        return (str(self.id) +'-'+ self.name)
admin.site.register(Product)
