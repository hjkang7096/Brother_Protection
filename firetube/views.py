from django.shortcuts import render
from .models import Video

def video_list(request):
    query = Video.objects.all()

    return render(request, "firetube/video_list.html", {
        "video_list":query,
        },
    )
