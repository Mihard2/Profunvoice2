import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.utils import timezone
from blog.models import (Longgrid,
                         Slider,
                         LonggridTag,
                         )



# Create your views here.

def index(request):
    now = timezone.now()    
    slide = Slider.objects.filter(public=True)
    longgrids = Longgrid.objects.all()
    return render(request, 'blog/index.html', {'slide': slide, 'longgrids': longgrids}) 

def longgrids(request):
    longgrids = Longgrid.objects.all()
    return render(request, 'blog/longgrids.html', {'longgrids': longgrids})

def longgrid_detail(request, slug):
    longgrid_detail = Longgrid.objects.get(slug=slug)
    return render(request, 'blog/longgrid_detail.html', {'page': longgrid_detail })

def longgrid_tag(request, slug):
    tag = LonggridTag.objects.get(slug=slug)
    longrids = tag.Longgrids.all()
    return render(request, 'blog/components/longgrid_tag.html', {'tag': tag , 'l':longrids })


# def NBA(request):
#     NBA = NBA.objects.all()
#     return render(request, 'blog/NBA.html', {'NBA': longgrids})




