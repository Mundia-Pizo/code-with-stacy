from django.urls import path, include
from .views import TopicListView, TopicDetailView, PostDetailView

urlpatterns = [
    path('blogs',TopicListView.as_view(), name='blogs'),
    path('<slug>/detail/',TopicDetailView.as_view(), name='topic-detail'),
    path('<topic_slug>/<post_slug>/',PostDetailView.as_view(), name='post-detail'),
]