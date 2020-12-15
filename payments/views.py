from django.shortcuts import render, redirect
from django.views.generic import View
from rave_python import Rave,RaveExceptions, Misc
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
from .forms import PaymentForm
import os

secretkey = os.environ.get('FLW_SECRETE_KEY')
publickey =os.environ.get('FLW_PUBLIC_KEY')
RAVE_ENCRYPTION_KEY =os.environ.get('FLW_ENC_KEY')
rave = Rave(publickey,secretkey,usingEnv=False)

class Payments(View):
    template_name = "payments/payment.html"
    def get(self,request):
        form=PaymentForm()
        return render(request, self.template_name, {"form":form})

    @method_decorator(csrf_exempt)
    def post(self,request):
        form =PaymentForm(request.POST)
        payload = {
        "cardno": "5438898014560229",
        "cvv": "276",
        "expirymonth": "09",
        "expiryyear": "25",
        "amount": "10",
        "email": "user@gmail.com",
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


class PaymentSuccess(CsrfExemptMixin, View):
    template_name='payments/payment_success.html'

    @method_decorator(csrf_exempt)    
    def get(self,request, *args, **kwargs):
        r = request.GET.get('response')
        # print("this is the response", r)
        import json
        r_dict=json.loads(r)
        status = r_dict['status']
        amount = r_dict['amount']
        print(status)
        print(amount)
        return render(request,self.template_name)


