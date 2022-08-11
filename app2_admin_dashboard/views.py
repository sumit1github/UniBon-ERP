from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from helpers.decorators import super_admin_only
app="app2_admin_dashboard/"

@method_decorator(super_admin_only, name='dispatch')
class AdminDashboard(View):
    template=app+"dashboard.html"
    def get(self,request):
        context={"form":''}
        return render(request,self.template,context)