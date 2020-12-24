from django.shortcuts import render, redirect
from django.views.generic import View
from rave_python import Rave,RaveExceptions, Misc
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from membership.views import get_user_membership, get_selected_membership
from .forms import PaymentForm
import json
import os

secretkey = os.environ.get('FLW_SECRETE_KEY')
publickey =os.environ.get('FLW_PUBLIC_KEY')
RAVE_ENCRYPTION_KEY =os.environ.get('FLW_ENC_KEY')
rave = Rave(publickey,secretkey,usingEnv=False)


'''
=============================================================================
WE WILL CREATE A METHOD THAT  WILL GET THE USER_SUBSCRITPION AND VALIDATE IT
=============================================================================
'''


class Payments(LoginRequiredMixin, View):
    template_name = "payments/payment.html"
    
    def get(self,request):
        selected_membership = get_selected_membership(request)
        form=PaymentForm()
        return render(request, self.template_name, {"form":form})

    @method_decorator(csrf_exempt)
    def post(self,request):
        form =PaymentForm(request.POST)
        selected_membership = get_selected_membership(request)
        # validate the form and perform the rest of the logic
        amount =str(selected_membership.price)
        if form.is_valid():
            cardno= str(form.cleaned_data.get('cardno'))
            expirymonth = str(form.cleaned_data.get('expirymonth'))
            expiryyear = str(form.cleaned_data.get('expiryyear'))
            cvv = str(form.cleaned_data.get('cvv'))
            email = str(request.user.email)
            name = str(request.user.username)
            print(amount)
            payload = {
            "cardno":cardno,
            "cvv": cvv,
            "expirymonth": expirymonth,
            "expiryyear": expiryyear,
            "amount": amount,
            "email": email,
            "phonenumber": "0902620185",
            "firstname": "temi",
            "lastname": "desola",
            "IP": "355426087298442",
            "redirect_url":"http://localhost:8000/payment/success"
            }

            try:
                res = rave.Card.charge(payload)
                if res['authUrl']:
                    return redirect(res['authUrl'])

                if res["suggestedAuth"]:
                    arg = Misc.getTypeOfArgsRequired(res["suggestedAuth"])

                    if arg == "pin":
                        Misc.updatePayload(res["suggestedAuth"], payload, pin="3310")
                    if arg == "address":
                        Misc.updatePayload(res["suggestedAuth"], payload, address= {"billingzip": "07205", "billingcity": "Hillside", "billingaddress": "470 Mundet PI", "billingstate": "NJ", "billingcountry": "US"})
                    
                    res = rave.Card.charge(payload)

                if res["validationRequired"]:
                    rave.Card.validate(res["flwRef"], "")

                res = rave.Card.verify(res["txRef"])
                print(res["transactionComplete"])

            except RaveExceptions.CardChargeError as e:
                print(e.err["errMsg"])
                print(e.err["flwRef"])

            except RaveExceptions.TransactionValidationError as e:
                print(e.err)
                print(e.err["flwRef"])

            except RaveExceptions.TransactionVerificationError as e:
                print(e.err["errMsg"])
                print(e.err["txRef"])
            return redirect('success')
        form=PaymentForm()
        return render(request, self.template_name, {"form":form})


class PaymentSuccess(CsrfExemptMixin,LoginRequiredMixin, View):
    template_name='payments/payment_success.html'

    @method_decorator(csrf_exempt)    
    def get(self,request, *args, **kwargs):
        r = request.GET.get('response')
        # print("this is the response", r
        r_dict=json.loads(r)
        status = r_dict['status']
        amount = r_dict['amount']
        print(status)
        print(amount)
        if r_dict['status'] == 'successful':
            return redirect('courses')
        else:
            return redirect('payment')
        return render(request,self.template_name)


