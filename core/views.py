from django.shortcuts import render
from django.views.generic import TemplateView, ListView,View, DetailView
from .models import Course, Lesson

class Home(TemplateView):
    template_name = 'core/home.html'


class CourseListView(ListView):
    model = Course
    template_name ='core/courses.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'core/course_detail.html'
    
class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'core/lesson_detail.html'

    