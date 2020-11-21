from django.urls import path, include
from .views import ArticleListView

urlpatterns = [
    path('blogs',ArticleListView.as_view(), name='blogs'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]