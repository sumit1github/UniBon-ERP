from django import forms
from .models import Copper

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model=Copper
        fields='__all__'
    sku_start=forms.CharField(required=True)
    name=forms.CharField(required=True)
    remarks=forms.CharField(required=True)

    sku_start.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter SKU starting code',"required":"required"})
    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Name',"required":"required"})
    remarks.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Remarks',"required":"required"})
   
    def clean(self):
        if self.cleaned_data['sku_start']:
            if (Product.objects.filter(sku_start=self.cleaned_data['sku_start'])).exists()==True:
                raise forms.ValidationError("Same SKU code is already present")
        else:
            raise forms.ValidationError("SKU code is needed")

    