from django.db import models
from django.contrib import admin

from app1_authentication.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class RMS(models.Model):
    Origin=(
        ('website','website'),
        ('erp','erp')
    )
    subject=models.TextField(default="No Subject")
    message_body=RichTextField(null=True,blank=True)
    file_data=models.FileField(upload_to='rms_files/', null=True,blank=True)

    date_of_creation=models.DateField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    coming_from=models.CharField(max_length=255,choices=Origin,null=True,blank=True)

    is_stared=models.BooleanField(default=False)
    is_read=models.BooleanField(default=False)
    add_to_recyle_bin=models.BooleanField(default=False)

    def __str__(self):
        return self.subject

admin.site.register(RMS)