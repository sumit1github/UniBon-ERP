# Generated by Django 4.0.6 on 2022-08-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app6_master', '0002_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('code_start_with', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
