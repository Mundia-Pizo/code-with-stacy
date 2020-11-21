from django.urls import path
from app_templates.views import CodeTemplateListView,CodeDetailView

urlpatterns=[
    path('temp/',CodeTemplateListView.as_view(), name='app_temp'),
    path('temp/<slug>/',CodeDetailView.as_view(), name='snippet-detail' )
]