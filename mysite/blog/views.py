from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blog.models import Post


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
