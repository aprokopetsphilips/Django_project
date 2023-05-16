from django.shortcuts import render
from django.views.generic.base import View

from my_blog.models import Post


# Create your views here.


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'my_blog/blog.html', {'post_list': posts})
