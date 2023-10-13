from django.shortcuts import render
from .models import Post
from django.http import Http404, HttpResponseRedirect
from blog.models import Post, Comment
from blog.forms import CommentForm
# Create your views here.
def list(request):
    Data = {'Posts':Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)

# def post(request, pk):
# dùng get_object_or_404 để tìm bài viết qua khóa chính, nên không thấy thì trả về 404.
#     post = get_object_or_404(Post, pk=pk)
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST, author=request.user, post=post)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(request.path)
#     return render(request, "blog/post.html", {'post': post, "form": form})

def post(request,id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404("Bài viết không tồn tại")
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {'post': post, "form": form})


