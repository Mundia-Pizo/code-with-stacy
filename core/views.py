from django.shortcuts import render
from django.views.generic import TemplateView, ListView,View, DetailView
from  membership.models import UserMembership
from .models import Course, Lesson

class Home(ListView):
    template_name = 'core/home.html'
    model=Course


class CourseListView(ListView):
    model = Course
    template_name ='core/courses.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'core/course_detail.html'
    
class LessonDetailView(View):
    def get(self,request, course_slug, lesson_slug, *args, **kwargs):
        course_qs=Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course=course_qs.first()

        lesson_qs=course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists(): 
            lesson=lesson_qs.first()

        user_membership = UserMembership.objects.filter(user=request.user).first()       
        user_membership_type=user_membership.membership.membership_type

        course_allowed_membership_types=course.allowed_membership.all()
        context={
            "object":None
        }
        if course_allowed_membership_types.filter(membership_type=user_membership_type).exists():
            context={
                 'object':lesson
             }
        return render(request, 'core/lesson_detail.html', context)


    