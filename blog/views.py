import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
from django.core.paginator import Paginator
from blog.models import (Longgrid,
                         Slider,
                         LonggridTag,
                         NBA,
                         NBATag
                         )



# Create your views here.

def index(request):
    now = timezone.now()    
    slide = Slider.objects.filter(public=True)
    longgrids = Longgrid.objects.all()
    nba = NBA.objects.all()
    return render(request, 'blog/index.html', {'slide': slide, 'longgrids': longgrids, 'nba': nba}) 

def longgrids(request):
    longgrids = Longgrid.objects.all()
    paginator = Paginator(longgrids, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginator = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'longgrids': page,
        'is_paginator': is_paginator,
        'prev_url': prev_url,
        'next_url': next_url
    }

    return render(request, 'blog/longgrids.html', context)

def longgrid_detail(request, slug):
    longgrid_detail = Longgrid.objects.get(slug=slug)
    return render(request, 'blog/components/longgrid_detail.html', {'page': longgrid_detail })

def longgrid_tag(request, slug):
    tag = LonggridTag.objects.get(slug=slug)
    longrids = tag.Longgrids.all()
    return render(request, 'blog/components/longgrid_tag.html', {'tag': tag , 'l':longrids })

def nba(request):
    nba = NBA.objects.all()
    paginator = Paginator(nba, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginator = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'nba': page,
        'is_paginator': is_paginator,
        'prev_url': prev_url,
        'next_url': next_url
    }

    return render(request, 'blog/NBA.html', context)

def nba_detail(request, slug):
    nba_detail = NBA.objects.get(slug=slug)
    return render(request, 'blog/components/nba_detail.html', {'page': nba_detail })

def nba_tag(request, slug):
    tag = NBATag.objects.get(slug=slug)
    nba = tag.NBA.all()
    return render(request, 'blog/components/nba_tag.html', {'tag': tag, 'n': nba})




