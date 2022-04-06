from django.shortcuts import render
from django.urls import reverse_lazy
from videoSurfers.models import Comment, VideoSurf
from django.views.generic import ListView, CreateView, DetailView
from .form import VideoForm
from .commentForm import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class IndexView(CreateView):
    model = VideoSurf
    template_name = 'index.html'
    fields = ['title','video']
    # success_url = reverse_lazy('index')
    


class ListView(LoginRequiredMixin ,ListView):
    model = VideoSurf
    context_object_name = 'video'
    template_name = 'list.html'
    fields='__all__'
    login_url = 'login'


class VideoDetailView(LoginRequiredMixin ,DetailView):
    model = VideoSurf
    context_object_name = 'video'
    template_name = 'video_detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comment_cnnt = Comment.objects.filter(
            video = self.get_object()).filter(is_active = True).order_by('author')
        data['comments'] = comment_cnnt
        if self.request.user.is_authenticated:
            data['comment_form'] = CommentForm(instance=self.request.user)
        return data
    

    def post(self, request, *args, **kwargs):
        new_comment = Comment(comment=request.POST.get('comment'),
                                  author=self.request.user,
                                  video=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)

    
        
