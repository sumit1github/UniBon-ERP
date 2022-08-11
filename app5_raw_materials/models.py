from django.db import models
from django.contrib import admin

class Copper(models.Model):
    sku_code=models.CharField(max_length=255,null=True,blank=True)
    date=models.CharField(max_length=255,null=True,blank=True)
    per_kg_price=models.FloatField(null=True,blank=True)

    def __str__(self):
        return (self.date)

admin.site.register(Copper)