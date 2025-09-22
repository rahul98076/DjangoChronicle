from django.contrib import admin
from .models import Post, Comment

# The @admin.register() decorator registers the model with the custom admin class
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # These fields will be displayed in the list view of posts
    list_display = ('title', 'slug', 'status', 'created_at')
    # This adds a filter sidebar
    list_filter = ('status',)
    # This adds a search bar
    search_fields = ['title', 'content']
    # This automatically fills the 'slug' field based on the 'title'
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    # This adds a custom action to the "Action" dropdown in the admin
    actions = ['approve_comments']

    # This defines the logic for our custom 'approve_comments' action
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)