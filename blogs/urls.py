from django.urls import path, include
from .views import PostDeletView, PostListView, PostDetailView, PostCreateView, PostUpdateView, SearchView, upload_image

urlpatterns = [
    path('upload/',upload_image, name='upload'),
    path('blogs/',PostListView.as_view(), name='blogs'),
    path('search/',SearchView.as_view(), name='search'),
    path('<slug>/detail/',PostDetailView.as_view(), name='post-detail'),
    path('<slug>/update/',PostUpdateView.as_view(), name='post-update'),
    path('<slug>/delete/',PostDeletView.as_view(), name='post-delete'),
    path('post-create/',PostCreateView.as_view(), name='post-create'),
]