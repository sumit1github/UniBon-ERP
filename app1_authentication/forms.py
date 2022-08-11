from django import forms
from .models import User, PerissionAssign

class UserCreationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','password2','first_name','last_name','contact_number','is_active',]

    username=forms.CharField(required = True)
    password=forms.CharField(required = True)
    password2=forms.CharField(required = True)
    first_name=forms.CharField(required = True)
    last_name=forms.CharField(required = True)
    is_active=forms.RadioSelect()
    is_staff=forms.RadioSelect()
    contact_number=forms.IntegerField()
    username.widget.attrs.update({'class': 'form-control','placeholder':'Enter UserName',"required":"required"})
    password.widget.attrs.update({'class': 'form-control','type':'password','placeholder':'Enter Password',"required":"required"})
    password2.widget.attrs.update({'class': 'form-control','type':'password','placeholder':'Confirm Password',"required":"required"})
    first_name.widget.attrs.update({'class': 'form-control','placeholder':'Enter first_name',"required":"required"})
    last_name.widget.attrs.update({'class': 'form-control','placeholder':'Enter last_name',"required":"required"})
    contact_number.widget.attrs.update({'type':'number','class': 'form-control','placeholder':'Enter Contact',"required":"required"})

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2'] :
            raise forms.ValidationError("PAssword is no same")
        # username=self.cleaned_data['username']
        # if not username:    
        #     raise forms.ValidationError("UserName Field CanNot Be Empty")

        # password=self.cleaned_data['password']
        # if not password:
        #     raise forms.ValidationError("Password Field CanNot Be Empty")

        # password=self.cleaned_data['password']
        # if not password:
        #     raise forms.ValidationError("Password Field CanNot Be Empty")

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
    username=forms.CharField()
    password=forms.CharField()

    username.widget.attrs.update({'autofocus':'autofocus' ,'class': 'form-control','placeholder':'Enter UserName',"required":"required"})
    password.widget.attrs.update({'class': 'form-control','type':'password','placeholder':'Enter Password',"required":"required"})
    def clean(self):

        username=self.cleaned_data['username']
        if not username:    
            raise forms.ValidationError("UserName Field CanNot Be Empty")

        password=self.cleaned_data['password']
        if not password:
            raise forms.ValidationError("Password Field CanNot Be Empty")

