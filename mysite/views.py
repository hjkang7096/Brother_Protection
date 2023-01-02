from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
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

