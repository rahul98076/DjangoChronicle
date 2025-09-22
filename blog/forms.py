from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        # This form is built from our Comment model
        model = Comment

        # These are the fields the user will see and fill out
        fields = ("name", "email", "body")
