from .models import myclass 
from django import forms

class myform(forms.ModelForm):
    class Meta:
        model = myclass 
        fields = "__all__"
        widgets = {
            "name":forms.TimeInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(render_value=True,attrs={"class":"form-control"}),
        }