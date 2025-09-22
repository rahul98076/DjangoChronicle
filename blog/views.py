from django.views import generic
from .models import Post

class PostList(generic.ListView):
    # This class-based view will handle displaying the list of all published posts.
    # We filter by status to ensure only 'published' posts are shown.
    # We order them by creation date, with the newest posts first.
    queryset = Post.objects.filter(status='published').order_by('-created_at')
    
    # We specify the template file that will be used to render this page.
    template_name = 'blog/post_list.html'

class PostDetail(generic.DetailView):
    # This view handles displaying a single, individual post.
    model = Post
    template_name = 'blog/post_detail.html'