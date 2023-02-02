from django.urls import path
from . import views

app_name = "firetube"

urlpatterns = [
    path("video_list/", views.video_list, name="video_list"),
    path("<int:pk>/", views.video_detail, name="video_detail"),
]
