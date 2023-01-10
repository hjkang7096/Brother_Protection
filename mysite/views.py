from django.shortcuts import render
from django.views.generic import TemplateView
import logging

logger = logging.getLogger("brother")

class IndexView(TemplateView):
    3/0 # 강제로 오류 발생
    logger.info("INFO 레벨로 출력")
    template_name = "index.html"


index_view = IndexView.as_view()


class AboutView(TemplateView):
    template_name = "about.html"


about_view = AboutView.as_view()


def page_not_found(request, exception):
    """
    404 page not found
    """
    return render(request, "404.html",{})

