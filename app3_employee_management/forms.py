from django import forms
from .models import Employee, EmployeeDocuments
from app6_master.models import Designation
 
class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        #exclude = ['designation']
    name=forms.CharField(required=True)
    address=forms.CharField(required=True)
    contact1=forms.IntegerField(required=True)
    contact2=forms.IntegerField()
    email=forms.EmailField()

    date_of_joining=forms.CharField(required=True)
    date_of_leaving=forms.CharField()

    addhar_number=forms.CharField(required=True)
    driving_lisence=forms.CharField(required=True)
    pan_card=forms.CharField(required=True)

    bank_ac_number=forms.CharField(required=True)
    ifsc_code=forms.CharField(required=True)

    working_hour=forms.CharField(required=True)
    basic_salary=forms.FloatField(required=True)
    extra_money=forms.FloatField(required=True)
    advance=forms.FloatField(required=True)
    designation=forms.ModelChoiceField(queryset=Designation.objects.all())
    locker_number=forms.CharField(required=True)
    extra_info=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Name',"required":"required"})
    address.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Address',"required":"required"})
    contact1.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'Enter Contact1',"required":"required"})
    contact2.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'Enter Contact2'})
    email.widget.attrs.update({'class': 'form-control','type':'email','placeholder':'Enter Contact2'})

    date_of_joining.widget.attrs.update({'class': 'form-control','data-datepicker':'','type':'text','id':'birthday','placeholder':'dd/mm/yyyy'})
    date_of_leaving.widget.attrs.update({'class': 'form-control','data-datepicker':'','type':'text','id':'birthday','placeholder':'dd/mm/yyyy'})

    addhar_number.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Aadhaar Number',"required":"required"})
    driving_lisence.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Driving Lisence'})
    pan_card.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Pan-card Number'})

    bank_ac_number.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Bank Account Number'})
    ifsc_code.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter IFSC Code'})

    working_hour.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'Enter Working Hour',"required":"required"})
    basic_salary.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'Enter Basic Salary',"required":"required"})
    extra_money.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'If getting Extra allowence'})
    advance.widget.attrs.update({'class': 'form-control','type':'number','placeholder':'If any Advance money'})
    designation.widget.attrs.update({'class': 'form-control','type':'text',"required":"required"})
    locker_number.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Loker Number',"required":"required"})
    extra_info.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Extra Information'})

class EmployeeDocumentForm(forms.ModelForm):
    class Meta:
        model=EmployeeDocuments
        fields=['name','file_data']
    name=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Document Name'})
