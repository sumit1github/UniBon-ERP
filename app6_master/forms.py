from django import forms
from .models import Designation, Unit, ItemCode

class DesignationCreationForm(forms.ModelForm):
    class Meta:
        model=Designation
        fields='__all__'
    
    name=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Designation',"required":"required"})

    def clean(self):
        if self.cleaned_data['name']:
            if (Designation.objects.filter(name=self.cleaned_data['name'])).exists()==True:
                raise forms.ValidationError("Same Designation is already present")
        else:
            raise forms.ValidationError("Designation is needed")

class UnitCreationForm(forms.ModelForm):
    class Meta:
        model=Unit
        fields='__all__'
    
    name=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Unit',"required":"required"})

    def clean(self):
        if self.cleaned_data['name']:
            if (Unit.objects.filter(name=self.cleaned_data['name'])).exists()==True:
                raise forms.ValidationError("Same Unit is already present")
        else:
            raise forms.ValidationError("Unit is needed")

class ItemCodeCreationForm(forms.ModelForm):
    class Meta:
        model=ItemCode
        fields='__all__'
    
    name=forms.CharField(required=True)
    code_start_with=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Name',"required":"required"})
    code_start_with.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Code Start With',"required":"required"})

    def clean(self):
        if self.cleaned_data['name']:
            if (ItemCode.objects.filter(name=self.cleaned_data['name'])).exists()==True:
                raise forms.ValidationError("Same name is already present")
        else:
            raise forms.ValidationError("name is needed")

        if self.cleaned_data['code_start_with']:
            if (ItemCode.objects.filter(code_start_with=self.cleaned_data['code_start_with'])).exists()==True:
                raise forms.ValidationError("Same code is already present")
        else:
            raise forms.ValidationError("code is needed")

class ItemCodeUpdateForm(forms.ModelForm):
    class Meta:
        model=ItemCode
        fields='__all__'
    
    name=forms.CharField(required=True)
    code_start_with=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Name',"required":"required"})
    code_start_with.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Code Start With',"required":"required"})
