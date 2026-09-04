from videos.models import VideoShare
from videos.models import VideoLike
from videos.models import VideoComment
from django.contrib import admin
from .models import *

admin .site.register(Video)
admin .site.register(VideoComment)
admin .site.register(VideoLike)
admin .site.register(VideoShare)
