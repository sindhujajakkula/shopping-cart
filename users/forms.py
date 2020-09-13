from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


user_type =( 
    ("Seller", "Seller"), 
    ("Customer", "Customer"), 
)

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    user_type = forms.ChoiceField(choices = user_type)
     
    

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']
