from django import forms
from django.db.models.fields import EmailField
from django.forms.widgets import EmailInput 
from .models import MailSubscription, Contact


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField(widget=EmailInput(attrs={
        'placeholder':'Enter email address'
    }))
    class Meta:
        model = MailSubscription
        fields="__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('email', 'subject', 'message')