from django.views.generic import ListView, DetailView
from blog.models import Post

class PostView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    context_object_name = "posts"

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
