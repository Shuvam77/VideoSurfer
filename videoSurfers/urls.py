from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.ListView.as_view(), name='list'),
    path('list/<int:pk>', views.VideoDetailView.as_view(), name='video_view'),

]