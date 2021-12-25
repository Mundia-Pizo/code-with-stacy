from django import forms
from .models import CoursePayment

class PaymentForm(forms.ModelForm):
    cardno      = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"42424242242242","class":"form-control input-control", "type":"text", "maxlength":"16"
    }))
    cvv         = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"851", "class":"form-control input-control", "type":"text", "maxlength":"3"
    }))
    expirymonth = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"mm","class":"form-control input-control", "type":"text", "maxlength":"2"
    }))
    expiryyear  = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"yy","class":"form-control input-control", "type":"text","maxlength":"2"
    }))

    class Meta:
        model = CoursePayment
        fields=('cardno', 'cvv', 'expirymonth', 'expiryyear')
