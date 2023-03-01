from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path(
        "post_list_category/<str:slug>/",
        views.post_list_category,
        name="post_list_category",
    ),
    path(
        "post_list_search/<str:search>/",
        views.post_list_search,
        name="post_list_search",
    ),
    path(
        "post_list_tag/<str:tag>/",
        views.post_list_tag,
        name="post_list_tag",
    ),
    path("post_new/", views.post_new, name="post_new"),
    path("post_update/<int:pk>/", views.post_update, name="post_update"),
    path("post_delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("<int:pk>/new_comment/", views.comment_new, name="new_comment"),
    path("comment_edit/<int:comment_pk>/", views.comment_edit, name="comment_edit"),
    path(
        # "comment_delete/<int:comment_pk>/", views.comment_delete, name="comment_delete"
        "comment_delete/",
        views.comment_delete,
        name="comment_delete",
    ),
]
