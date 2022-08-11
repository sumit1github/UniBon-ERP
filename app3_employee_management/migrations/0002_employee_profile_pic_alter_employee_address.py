# Generated by Django 4.0.6 on 2022-07-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3_employee_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
