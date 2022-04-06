from django.contrib import admin

from videoSurfers.models import VideoSurf, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment

class VideoSurfAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    list_display = ('id','title')
    readonly_field = ('slug')

admin.site.register(VideoSurf, VideoSurfAdmin)
