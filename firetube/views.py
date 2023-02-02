from django.shortcuts import render, get_object_or_404
from .models import Video, Comment
from django.core.paginator import Paginator


def video_list(request):
    query = Video.objects.all()
    page = int(request.GET.get("page", 1))  # 두번째 인자 : 없을 시 디폴트 값
    paginator = Paginator(query, 3, allow_empty_first_page=True)
    page_obj = paginator.page(page)
    categories = Category.objects.all()
    total_category_post_count = Post.objects.all().count()
    no_category_post_count = Post.objects.filter(category=None).count()

    return render(
        request,
        "firetube/video_list.html",
        {
            "video_list": query,
            "page_obj": page_obj,
            "paginator": paginator,
        },
    )


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)

    return render(
        request,
        "firetube/video_detail.html",
        {
            "video": video,
        },
    )
