from django.shortcuts import render
from django.views.generic import ListView, DetailView,View
from .models import Article, Topic


class  TopicListView(ListView):
    model = Topic
    template_name = 'blogs/topic_list.html'


class TopicDetailView(DetailView):
    model = Topic
    template_name ='blogs/topic_detail.html'

class PostDetailView(View):
    template_name= 'blogs/post_detail.html'
    def get(self, request, topic_slug, post_slug,*args, **kwargs):
        topic_qs = Topic.objects.filter(slug=topic_slug)

        if topic_qs.exists():
            topic =topic_qs.first()

        post_qs = topic.articles.filter(slug=post_slug)
        if post_qs.exists():
            post=post_qs.first()

        context={
           'post':post
        }
        return render(request, self.template_name, context)