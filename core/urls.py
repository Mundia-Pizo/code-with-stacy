from django.urls import path
from .views import (
    Home, 
    CourseListView, 
    CourseDetailView, 
    LessonDetailView,
    About, ContactView,
    ProjectDetail, 
    Thanks,
    # SubsriptionView
    )

urlpatterns=[
    path('',Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('courses', CourseListView.as_view(), name='courses'),
    path('<int:pk>/project-detail/', ProjectDetail.as_view(), name='project-detail'),
    path('thanks/', Thanks.as_view(), name='thanks'),
    path('course/<slug>/', CourseDetailView.as_view(), name='course-details'),
    path('lesson/<course_slug>/<lesson_slug>/', LessonDetailView.as_view(), name='lesson-details')
]