from django import forms
from .models import User,Keijiban
from django.contrib.auth.forms import UserCreationForm

class KeijibanForm(forms.ModelForm) :
    class Meta :
        model = Keijiban
        fields = "__all__"

class CreateForm(forms.ModelForm):
    class Meta :
        model = Keijiban
        fields = ["toukou","image","created_at"]

class ProfileForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["email","age","sex","address","icon"]


class SignupForm(UserCreationForm):
    class Meta :
        model = User
        fields = ["username","password1","password2"]

class LoginForm(forms.ModelForm) :
    class Meta :
        model = User
        fields = ["username","password"]
