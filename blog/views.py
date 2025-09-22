from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status="published").order_by("-created_at")
    template_name = "blog/post_list.html"


def post_detail(request, slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by("created_at")
    new_comment = None

    # Check if the request is a POST (i.e., the form was submitted)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create a Comment object but don't save to the database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Now, save the comment to the database
            new_comment.save()
    else:
        # If it's a GET request, just create a blank form
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
