from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import (
    Membership, 
    UserMembership, 
    Subscription)

def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

def get_user_subscritpion(request):
    user_subscription_qs = Subscription.objects.filter(user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription=user_subscription_qs.first()
        return user_subscription
    return None

def get_selected_membership(request):
    membership_type= request.session.get('selected_membership_type')
    selected_membership_qs=Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None


class  MemebershipSelectView(View):
    model = Membership
    template_name = 'membership/membership.html'
    def get(self, request):
        memberships = Membership.objects.filter(membership_type='Professional')
        context={
            'memberships':memberships
        }
        return render(request, self.template_name, context)

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership =get_user_membership(self.request)
        context['current_membership']=str(current_membership)
        return context

    def post(self, request,*args, **kwargs):
        selected_membership_type = request.POST.get('membership_type') 
        user_membership =get_user_membership(request)
        user_subscription = get_user_subscritpion(request)

        selected_membership_qs=Membership.objects.filter(
            membership_type=selected_membership_type
        )
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()


        '''
        ==========
        VALIDATION
        ==========
        '''
        if user_membership.membership == selected_membership:
            if user_subscription !=None:
                messages.info(request, 'Thank you for subscribing')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        request.session['selected_membership_type']=selected_membership.membership_type
        
        return HttpResponseRedirect(reverse('payment'))