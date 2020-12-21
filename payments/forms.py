from django import forms
from .models import CoursePayment

class PaymentForm(forms.ModelForm):
    cardno      = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"42424242242242"
    }))
    cvv         = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"851"
    }))
    expirymonth = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"mm"
    }))
    expiryyear  = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"yy"
    }))

    class Meta:
        model = CoursePayment
        fields='__all__'
