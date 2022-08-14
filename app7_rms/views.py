from django.shortcuts import render, redirect, HttpResponse
from django.views import View

from .forms import RMSCreationForm
from .models import RMS

from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from helpers.decorators import super_admin_only, login_required, product_edit_permission
from helpers.pagination import paginate
import os


app="app7_rms/" 
# Create your views here.


# Create your views here.
@method_decorator(login_required,name='dispatch')
class RMSView(View):
    model=RMS
    form=RMSCreationForm
    template=app+"rms_list.html"

    def get(self,request,*args,**kwargs):
        message_list=[]
        if request.user.is_authenticated:
            user=request.user

            # admin can see all messages
            if user.is_staff==False:
                message_list=self.model.objects.filter(created_by=request.user).order_by('-id')              
                message_list=paginate(request, message_list, 50)

            elif user.is_staff==True:
                # users can see only there messages
                message_list=self.model.objects.filter(is_read=False,add_to_recyle_bin=False,is_stared=False).order_by('-id')
                message_list=paginate(request, message_list, 50)

            else:
                message_list=[]
        context={'form':self.form, 'message_list':message_list}
        return render(request,self.template,context)
    
    def post(self,request,*args,**kwargs):

        form=self.form(request.POST, request.FILES)
        if form.is_valid():
            data=form.save()

            # from where the message is coming like erp, application, website
            if request.POST.get('coming_from'):
                data.coming_from=request.POST.get('coming_from')

            if request.user.is_authenticated:
                data.created_by=request.user

            data.save()
            messages.success(request, "Message has been sent, Please wait for reply ..")
        else:
            messages.error(request,"Messave save error : "+str(form.errors))

        return redirect('app7_rms:rms_list_or_create')


@method_decorator(super_admin_only,name='dispatch')
class RMSOperationView(View):
    model=RMS
    form=RMSCreationForm
    template=app+"rms_list.html"

    def get(self,request,*args,**kwargs):

        m_id=kwargs.get('m_id')
        operation=kwargs.get('operation')

        message=self.model.objects.get(id=m_id)

        if operation=="read":

            if message.is_read==False:
                message.is_read=True
                messages.success(request, "Done: Maked As Read")
            else:
                message.is_read=False
                messages.success(request, "Done: Maked As Un-read")
            
            message.save()
        
        elif operation == 'star':

            if message.is_stared==False:
                message.is_stared=True
                messages.success(request, "Done: Maked As Important")
            else:
                message.is_stared=False
                messages.success(request, "Done: Remove As Important")
            
            message.save()
        
        elif operation == 'recyle':

            if message.add_to_recyle_bin==False:
                message.add_to_recyle_bin=True
                messages.success(request, "Done: Added To Recycle-Bin")
            else:
                message.add_to_recyle_bin=False
                messages.success(request, "Done: messaged is restored.")
            
            message.save()
        
        elif operation == 'delete':
            if message.file_data:
                if len(message.file_data) > 0:
                    os.remove(message.file_data.path)
            message.delete()
            messages.success(request, "Message is Deleted ..")

        else:
            messages.error(request, "Invadid Operation !")

        return redirect('app7_rms:rms_list_or_create')


@method_decorator(login_required,name='dispatch')
class RMSFilterView(View):
    model=RMS
    form=RMSCreationForm
    template=app+"rms_list.html"

    def get(self,request,*args,**kwargs):
        filter_name=kwargs.get('filter')
        data_list=[]

        if filter_name=="unread":
            data_list=self.model.objects.filter(is_read=False)

        elif filter_name=="read":
            data_list=self.model.objects.filter(is_read=True)

        elif filter_name=="recycle":
            data_list=self.model.objects.filter(add_to_recyle_bin=True)

        elif filter_name=="stared":
            data_list=self.model.objects.filter(is_stared=True)
        else:
            messages.error(request, "Enter a Valid Filter !")
        
        message_list=paginate(request, data_list, 50)
        context={'form':self.form, 'message_list':message_list}
        return render(request,self.template,context)