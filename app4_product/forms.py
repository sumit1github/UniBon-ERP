from django import forms
from .models import Product
from app6_master.models import Unit, ItemCode

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

    name=forms.CharField(required=True)
    # Item_code=forms.ChoiceField(choices=[(i.pk, i) for i in ItemCode.objects.all()])
    # unit=forms.ChoiceField(choices=[(u.pk, u) for u in Unit.objects.all()])
    Item_code=forms.ModelChoiceField(queryset=ItemCode.objects.all())
    unit=forms.ModelChoiceField(queryset=Unit.objects.all())
    remarks=forms.CharField(required=True)

    name.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Name',"required":"required"})
    Item_code.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Remarks',"required":"required"})
    unit.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Remarks',"required":"required"})
    remarks.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Remarks',"required":"required"})
   
    # def clean(self):
    #     if self.cleaned_data['sku_start']:
    #         if (Product.objects.filter(sku_start=self.cleaned_data['sku_start'])).exists()==True:
    #             raise forms.ValidationError("Same SKU code is already present")
    #     else:
    #         raise forms.ValidationError("SKU code is needed")

    