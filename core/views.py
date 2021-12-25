from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView, ListView, View, DetailView
from django.http import HttpResponseRedirect
from membership.models import UserMembership
from .models import Course, MailSubscription, Project
from django.contrib.auth.mixins import LoginRequiredMixin
from core.sub_form import SubscriptionForm, ContactForm
from django.views.generic.edit import FormView
from blogs.models import Article


class Home(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        latest_articles = Article.objects.order_by('-timestamp')[0:4]
        form = SubscriptionForm()
        context = {
            'projects': projects,
            'latest_articles': latest_articles,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscription_email = MailSubscription.objects.filter(email=email)
            if subscription_email.exists():
                pass
            else:
                form.save()
        form = SubscriptionForm()
        return render(request, self.template_name, {'form': form})


class About(View):
    template_name = 'core/about_bio.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        return render(request, self.template_name, {'projects': projects})


class ProjectDetail(DetailView):
    model = Project
    template_name = 'core/project-detail.html'


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = 'thanks'

    def form_valid(self, form):
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # sender = form.cleaned_data['sender']
            from_mail = form.cleaned_data['email']
            # cc_myself = form.cleaned_data['cc_myself']
            recipients = ('mundiapizos@gmail.com',)
            # if cc_myself:
            #     recipients.append(sender)
        send_mail(subject, message, from_mail, recipients)
        return HttpResponseRedirect('/thanks/')


class Thanks(TemplateView):
    template_name = 'core/thanks.html'


class CourseListView(ListView):
    model = Course
    template_name = 'core/courses.html'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'core/course_detail.html'


class LessonDetailView(LoginRequiredMixin, View):
    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()

        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()

        user_membership = UserMembership.objects.filter(
            user=request.user).first()
        user_membership_type = user_membership.membership.membership_type

        course_allowed_membership_types = course.allowed_membership.all()
        context = {
            "object": None
        }
        if course_allowed_membership_types.filter(membership_type=user_membership_type).exists() or course_allowed_membership_types.filter(membership_type='Free'):
            context = {
                'object': lesson
            }
        else:
            return redirect('membership')
        return render(request, 'core/lesson_detail.html', context)
