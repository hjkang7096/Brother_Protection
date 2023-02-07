from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Video, Comment, Category
from django.core.paginator import Paginator
from .forms import CommentForm
from django.contrib import messages


def video_list(request):
    query = Video.objects.all()
    page = int(request.GET.get("page", 1))  # 두번째 인자 : 없을 시 디폴트 값
    paginator = Paginator(query, 2, allow_empty_first_page=True)
    page_obj = paginator.page(page)
    categories = Category.objects.all()
    total_category_post_count = Video.objects.all().count()
    no_category_post_count = Video.objects.filter(category=None).count()

    return render(
        request,
        "firetube/video_list.html",
        {
            "video_list": query,
            "page_obj": page_obj,
            "paginator": paginator,
            "categories": categories,
            "total_category_count": total_category_post_count,
            "no_category_count": no_category_post_count,
        },
    )


def video_list_category(request, slug):
    if slug != "기 타":
        query = Video.objects.filter(category__name__contains=slug)
    else:
        query = Video.objects.filter(category=None)

    page = int(request.GET.get("page", 1))  # 두번째 인자 : 없을 시 디폴트 값
    paginator = Paginator(query, 2, allow_empty_first_page=True)
    page_obj = paginator.page(page)
    categories = Category.objects.all()
    total_category_post_count = Video.objects.all().count()
    no_category_post_count = Video.objects.filter(category=None).count()

    return render(
        request,
        "firetube/video_list.html",
        {
            "video_list": query,
            "page_obj": page_obj,
            "paginator": paginator,
            "categories": categories,
            "total_category_count": total_category_post_count,
            "no_category_count": no_category_post_count,
            "slug": slug,
        },
    )


def video_list_search(request, search):
    query = Video.objects.filter(
        Q(title__icontains=search) | Q(description__icontains=search)
    )

    page = int(request.GET.get("page", 1))  # 두번째 인자 : 없을 시 디폴트 값
    paginator = Paginator(query, 2, allow_empty_first_page=True)
    page_obj = paginator.page(page)
    categories = Category.objects.all()
    total_category_post_count = Video.objects.all().count()
    no_category_post_count = Video.objects.filter(category=None).count()

    return render(
        request,
        "firetube/video_list.html",
        {
            "video_list": query,
            "page_obj": page_obj,
            "paginator": paginator,
            "categories": categories,
            "total_category_count": total_category_post_count,
            "no_category_count": no_category_post_count,
            "search": search,
        },
    )


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    categories = Category.objects.all()
    total_category_post_count = Video.objects.all().count()
    no_category_post_count = Video.objects.filter(category=None).count()
    comment_form = CommentForm()

    return render(
        request,
        "firetube/video_detail.html",
        {
            "video": video,
            "comment_form": comment_form,
            "categories": categories,
            "total_category_count": total_category_post_count,
            "no_category_count": no_category_post_count,
        },
    )


def comment_new(request, pk):
    if request.user.is_authenticated:
        video = get_object_or_404(Video, pk=pk)

        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.video = video
                comment.save()
                return redirect("firetube:video_detail", video.pk)
        else:
            comment_form = CommentForm()
    else:
        raise PermissionDenied

    return redirect(
        request,
        "firetube/comment_form.html",
        {
            "comment_form": comment_form,
            "video": video,
        },
    )


# def comment_edit(request, comment_pk):
#     if request.user.is_authenticated:
#         comment = get_object_or_404(Comment, pk=comment_pk)
#         post = comment.post
#
#         if request.method == "POST":
#             comment_form = CommentForm(request.POST, instance=comment)
#             if comment_form.is_valid():
#                 comment = comment_form.save(commit=False)
#                 comment.author = request.user
#                 comment.post = post
#                 comment.save()
#                 return redirect(post.get_absolute_url())
#         else:
#             comment_form = CommentForm(instance=comment)
#     else:
#         raise PermissionDenied
#
#     return render(
#         request,
#         "blog/comment_edit.html",
#         {
#             "comment_form": comment_form,
#             "comment": comment,
#         },
#     )


@login_required
def comment_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        messages.success(request, "댓글을 삭제했습니다.")
        return redirect(comment.video.get_absolute_url())
    else:
        raise PermissionDenied
