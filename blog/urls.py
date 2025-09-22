from django.urls import path
from . import views

# This is good practice for namespacing and will be useful later.
app_name = 'blog'

urlpatterns = [
    # When a user visits the root URL (''), show the PostList view.
    path('', views.PostList.as_view(), name='post_list'),
    
    # When a user visits a URL like '/my-awesome-post/', show the PostDetail view.
    # The <slug:slug> part captures the text from the URL and passes it to the view.
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]