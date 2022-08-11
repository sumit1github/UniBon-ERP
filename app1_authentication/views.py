from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.template.loader import render_to_string
from .forms import LoginForm, UserCreationForm
from .models import User, PerissionAssign
from django.contrib import messages
from django.contrib.auth.models import Permission

from django.contrib.auth.models import auth
from django.contrib.auth.hashers import check_password, make_password
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers.decorators import super_admin_only
app="app1_authentication/"

class Login(View):
    form=LoginForm
    model=User
    template=app+"login.html"
    #template="master/master.html"
    def get(self,request):
        context={"form":self.form}
        return render(request,self.template,context)
    
    def post(self,request):
        data=request.POST
        form_data=self.form(data)
        if form_data.is_valid():  
            user=auth.authenticate(username=data['username'], password=data['password'])
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'successfully Login.') 
            if user.is_staff==True:
                return redirect('/admin_dashboard/')
        else:
            messages.error(request, 'Login Failed') 
        return redirect('/login')


@method_decorator(login_required, name='dispatch')
class LogOut(View):
    def get(self,request):
        auth.logout(request)
        messages.success(request, 'successfully Logout.')
        return redirect('/login')


@method_decorator(super_admin_only, name='dispatch')
class UserList(View):
    html="app1_authentication/users/user_list.html"
    def get(self,request):
        all_users=User.objects.all()
        context={'user_list':all_users,}
        return render(request,self.html,context)

@method_decorator(super_admin_only, name='dispatch')
class UserCreation(View):
    form=UserCreationForm
    html="app1_authentication/users/create_user.html"
    def get(self,request):
        context={'form':self.form}
        return render(request,self.html,context)
    
    def post(self,request):
        form_data=self.form(request.POST)
        if form_data.is_valid():
            
            f_data=form_data.save(commit=False)
            f_data.password=make_password(request.POST.get('password'))
            f_data.save()

            messages.success(request, "Data is saved with no errors.")
        else:

            messages.error(request,str  (form_data.errors))
        context={'form':self.form}
        return render(request,self.html,context)

@method_decorator(super_admin_only, name='dispatch')
class UserPasswordChange(View):
    def post(self,request,*args,**kwargs):
        obj=User.objects.get(id=kwargs.get("u_id"))
        password=request.POST.get('password')
        obj.password=make_password(password)
        obj.save()
        messages.success(request,"Password is Changed succesfully.")
        return redirect('app1_authentication:user_list')

@method_decorator(super_admin_only, name='dispatch')
class UserStateChange(View):
    def get(self,request,*args,**kwargs):
        obj=User.objects.get(id=kwargs.get("u_id"))
        if kwargs.get("state")=="active":
            obj.is_active=True
        else:
            obj.is_active=False
        obj.save()
        messages.success(request,"Users state is changed now.")
        return redirect('app1_authentication:user_list')

@method_decorator(super_admin_only, name='dispatch')
class UserPermissionAdd(View):
    model=PerissionAssign
    def post(self,request,*args,**kwargs):
        obj=User.objects.get(id=kwargs.get("u_id"))
        p_name=request.POST.get('permission')
        if (self.model.objects.filter(user=obj,name=p_name).exists())==True:
            messages.error(request,'Permission Is already present')
        else:
            self.model.objects.create(user=obj,name=p_name)
            messages.success(request,"Permission Is Added")
        return redirect('app1_authentication:user_list')

@method_decorator(super_admin_only, name='dispatch')
class Update_user(View):
    form=UserCreationForm
    html="app1_authentication/users/create_user.html"
    def get(self,request):
        context={'form':self.form}
        return render(request,self.html,context)
    def put(self,request):
        pass