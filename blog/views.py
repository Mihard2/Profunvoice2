import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
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
    return render(request, 'blog/longgrids.html', {'longgrids': longgrids})

def longgrid_detail(request, slug):
    longgrid_detail = Longgrid.objects.get(slug=slug)
    return render(request, 'blog/components/longgrid_detail.html', {'page': longgrid_detail })

def longgrid_tag(request, slug):
    tag = LonggridTag.objects.get(slug=slug)
    longrids = tag.Longgrids.all()
    return render(request, 'blog/components/longgrid_tag.html', {'tag': tag , 'l':longrids })

def nba(request):
    nba = NBA.objects.all()
    return render(request, 'blog/NBA.html', {'nba': nba})

def nba_detail(request, slug):
    nba_detail = NBA.objects.get(slug=slug)
    return render(request, 'blog/components/nba_detail.html', {'page': nba_detail })

def nba_tag(request, slug):
    tag = NBATag.objects.get(slug=slug)
    nba = tag.NBA.all()
    return render(request, 'blog/components/nba_tag.html', {'tag': tag, 'n': nba})




