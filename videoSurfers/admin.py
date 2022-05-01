from django.contrib import admin

from videoSurfers.models import VideoSurf, Comment
from video_encoding.admin import FormatInline

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment

class VideoSurfAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        FormatInline,
    ]
    list_display = ('id','title', 'width', 'height', 'duration')
    fields = ('slug', 'video', 'width', 'height', 'duration')
    readonly_fields = fields
admin.site.register(VideoSurf, VideoSurfAdmin)
