from django.db.models import Q
from django.shortcuts import render
from wagtail.wagtailcore.models import Page


def sitemap(request):
    pages = Page.objects.all().exclude(Q(depth__iexact=1) | Q(depth__iexact=2))

    return render(request, 'sitemap/sitemap.html', {
        'pages': pages,
    })
