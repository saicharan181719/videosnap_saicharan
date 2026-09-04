from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Video


@login_required
def create_video_view(request):

    if request.method == "POST":

        title = request.POST.get("title_html")
        description = request.POST.get("description_html")
        video_file = request.FILES.get("video")

        Video.objects.create(
            user=request.user,
            title=title,
            description=description,
            video=video_file,
        )

        return redirect("videos")

    return render(request, "videoss/create-video.html")


@login_required
def videos_view(request):

    videos = Video.objects.all().order_by("-created_at")

    return render(
        request,
        "videoss/videos.html",
        {
            "videos_all": videos
        }
    )