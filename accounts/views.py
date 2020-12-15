from django.shortcuts import render,redirect
from .accounts_forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    context={
        'form':form
    }
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', context)
    return render(request, 'accounts/register.html', context)
        
    

