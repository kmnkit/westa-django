from django import forms
from .models import Comment


class CreateCommentForm(forms.ModelForm):
    text = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "댓글을 입력해 주세요.",
                "size": 140,
                "class": "focus:ring-0 border-0",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ("text",)

    def save(self):
        return super().save(commit=False)
