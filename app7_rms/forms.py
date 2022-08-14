from django import forms
from .models import RMS
    
class RMSCreationForm(forms.ModelForm):
    class Meta:
        model=RMS
        fields=['subject','message_body','file_data']
    
    subject=forms.CharField(required=True)
    message_body=forms.TextInput()

    subject.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Subject',"required":"required"})
    #message_body.widget.attrs.update({'class': 'form-control','type':'text','placeholder':'Enter Message',"required":"required"})
