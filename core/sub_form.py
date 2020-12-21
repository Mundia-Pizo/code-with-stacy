from django import forms 
from .models import MailSubscription


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = MailSubscription
        fields="__all__"
