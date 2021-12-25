from django.shortcuts import render,redirect
from .accounts_forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import( UserRegistrationForm,
                     UserUpdateForm, 
                    ProfileUpdateForm)
from django.contrib.auth.decorators import login_required

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

# def register(request):
# 	if request.method=='POST':
# 		form = UserRegistrationForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			username = form.cleaned_data.get('username')
# 			messages.success(request,f"Account created succesfully. Please login here")
# 			return redirect('login')
# 	else:
# 		form = UserRegistrationForm()
# 	return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		user_form =UserUpdateForm(request.POST ,instance=request.user)
		profile_form = ProfileUpdateForm(request.POST,
			request.FILES,
			instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request,f"Account updated succesfully")
			return redirect('profile')
	else:
		user_form =UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)


	context ={
	'user_form':user_form,
	'profile_form':profile_form
	}

	return render(request, 'accounts/profile.html', context)




