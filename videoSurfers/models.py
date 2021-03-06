from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation
from video_encoding.fields import VideoField
from video_encoding.models import Format


# Create your models here.

class VideoSurf(models.Model):
    class Meta:
        verbose_name_plural = 'VideoSurfs'
        verbose_name = 'VideoSurf'

    title = models.CharField (max_length=200, blank=False, null=True)
    width = models.PositiveIntegerField(editable=False, null=True)
    height = models.PositiveIntegerField(editable=False, null=True)
    duration = models.FloatField(editable=False, null=True)
    video = VideoField(width_field='width', height_field='height',
                     duration_field='duration', upload_to='videos', verbose_name='video')
    slug = models.SlugField(null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    format_set = GenericRelation(Format)

        
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(VideoSurf, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    @property
    def number_of_comment(self):
        return Comment.objects.filter(video=self)

    def get_absolute_url(self):
        return reverse('video_view', kwargs={'pk': str(self.pk)})

    

class Comment(models.Model):
    video= models.ForeignKey(
        VideoSurf, on_delete=models.CASCADE, related_name='comments'
    )
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.comment}'