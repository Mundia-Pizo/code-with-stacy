from django import forms
from .models import CoursePayment

class PaymentForm(forms.ModelForm):
    cardno      = forms.IntegerField()
    cvv         = forms.IntegerField()
    expirymonth = forms.IntegerField()
    expiryyear  = forms.IntegerField()

    class Meta:
        model = CoursePayment
        fields='__all__'
