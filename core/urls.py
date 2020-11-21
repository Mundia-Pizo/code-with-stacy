from django.urls import path
from .views import Home, CourseListView, CourseDetailView, LessonDetailView

urlpatterns=[
    path('',Home.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('course/<slug>/', CourseDetailView.as_view(), name='course-details'),
    path('lesson/<course_slug>/<lesson_slug>/', LessonDetailView.as_view(), name='lesson-details')
]