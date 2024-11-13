from django.forms import ModelForm, PasswordInput
from .models import User

class UserForm(ModelForm): 
    class Meta:
        model = User
        widgets = {
            'password': PasswordInput()
        }
