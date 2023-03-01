from django.urls import path
from . import views

app_name = "firetube"

urlpatterns = [
    path("video_list/", views.video_list, name="video_list"),
    path(
        "video_list_category/<str:slug>/",
        views.video_list_category,
        name="video_list_category",
    ),
    path(
        "video_list_search/<str:search>/",
        views.video_list_search,
        name="video_list_search",
    ),
    path("<int:pk>/", views.video_detail, name="video_detail"),
    path("<int:pk>/new_comment/", views.comment_new, name="new_comment"),
    path(
        # "comment_delete/<int:comment_pk>/", views.comment_delete, name="comment_delete"
        "comment_delete/",
        views.comment_delete,
        name="comment_delete",
    ),
]
