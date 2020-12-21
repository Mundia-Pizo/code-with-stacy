from django.shortcuts import render,redirect
from .accounts_forms import RegistrationForm

# def register(request):
#     form = RegistrationForm()
#     context={
#         'form':form
#     }
#     if request.method=="POST":
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     return render(request, 'accounts/register.html', context)
        
    
from django.views.generic.edit import FormView

class RegistrationView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = 'login'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super().form_valid(form)








