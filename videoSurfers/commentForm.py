from django import forms
from videoSurfers.models import Comment




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']