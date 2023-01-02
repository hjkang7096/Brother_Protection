from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django_pydenticon.views import image as pydenticon_image
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.urls import re_path
from . import views



urlpatterns = [
    path("", views.index_view, name="root"),
    path("about/", views.about_view, name="about"),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("accounts/", include("accounts.urls")),
    path("board1/", include("board1.urls")),
    path("board2/", include("board2.urls")),
    path("identicon/image/<path:data>/", pydenticon_image, name="pydenticon_image"),
    path("summernote/", include("django_summernote.urls")),
    path("tinymce/", include("tinymce.urls")),
    # 비밀번호 재설정을 위하여 추가된 코드
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # debug = False : media file을 불러오지 못하는 문제 해결
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # debug = False : static file을 불러오지 못하는 문제 해결
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

handler404 = "mysite.views.page_not_found"





# azure에는 media, static을 설정해주기 때문에 if settings.DEBUG: 필요
# urlpatterns += \
#     static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += \
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





