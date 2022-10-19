from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

#ModelForm is only for creating and updating data in the database!!
class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput()
        }


class UserSigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
