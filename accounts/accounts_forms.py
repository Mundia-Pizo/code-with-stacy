from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class RegistrationForm(UserCreationForm):
#     email=forms.EmailField()

#     class Meta:
#         model = User
#         fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username', 'email')

    # def clean(self):
    #     cleaned_data = super(RegistrationForm, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")

    #     if password != confirm_password:
    #         self.add_error('confirm_password',"Password does not match")

    #     return cleaned_data