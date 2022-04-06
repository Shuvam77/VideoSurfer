from django import forms
from videoSurfers.models import VideoSurf


class VideoForm(forms.ModelForm):
    
    class Meta:
        model = VideoSurf
        fields = ['title', 'video']