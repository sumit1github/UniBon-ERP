from functools import wraps
from django.http import HttpResponseRedirect
from django.contrib import messages
from app1_authentication.models import PerissionAssign

'''
for admin only
'''
def super_admin_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    if request.user.is_authenticated:
        profile = request.user
        if profile.is_staff == True:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')
    messages.error(request,"You are not login !")
    return HttpResponseRedirect('/login')
  return wrap

'''
for login only
'''
def login_required(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    if request.user.is_authenticated:
      return function(request, *args, **kwargs)
    else:
      return HttpResponseRedirect('/')
    messages.error(request,"You are not login !")
    return HttpResponseRedirect('/login')
  return wrap

'''
for permission only
'''


# def employee_edit_permission(function):
#   @wraps(function)
#   def wrap(request, *args, **kwargs):
#     if request.user.is_staff==True or (PerissionAssign.objects.filter(user=request.user,name='employee_manage').exists())==True:
#       return function(request, *args, **kwargs)
#     else:
#       messages.error(request,"Unauthorized Access contact Admin for access")
#       return HttpResponseRedirect('/login')    
#   return wrap

def employee_edit_permission(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    user=request.user
    if user.is_staff==True or (PerissionAssign.objects.filter(user=user,name='employee_manage').exists())==True:
      return function(request, *args, **kwargs)
    else:
      return HttpResponseRedirect('/')
    messages.error(request,"You are not login !")
    return HttpResponseRedirect('/login')
  return wrap
  


def product_edit_permission(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
    user=request.user
    if user.is_staff==True or (PerissionAssign.objects.filter(user=user,name='product_edit').exists())==True:
      return function(request, *args, **kwargs)
    else:
      return HttpResponseRedirect('/')
    messages.error(request,"You are not login or Don't have access !")
    return HttpResponseRedirect('/login')
  return wrap