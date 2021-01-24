from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("description", "photo")

    def save(self):
        post = super().save(commit=False)
        post.user = self.request.user
        return post
