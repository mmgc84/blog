from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")


def detail(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)
