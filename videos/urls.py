from django.urls import path
from . import views

urlpatterns = [

    path("create-video/",views.create_video_view,name="create-video"),
    path("videos/",views.videos_view,name="videos"),
]