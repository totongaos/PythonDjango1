from django.shortcuts import render
from .models import Post
from django.http import Http404
# Create your views here.
def list(request):
    Data = {'Posts':Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)

def post(request,id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")

    return render(request, 'blog/post.html', {'post':post})