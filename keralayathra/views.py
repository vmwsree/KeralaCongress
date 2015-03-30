
from django.core.context_processors import csrf

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from models import *
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index_4.htm', c)
def keralayathra(request):
    c = {}
    days = keralaYatra.objects.all()
    c={'YathraStop':days}
    c.update(csrf(request))
    return render_to_response('keralayathra.htm', c)
def yathraDay(request,day_id):
    c = {}
    c.update(csrf(request))
    return render_to_response('home.html', c)
def gallery(request):
    imagelist = images.objects.all()
    c = {"images":imagelist}
    c.update(csrf(request))
    return render_to_response('page-gallery.htm', c)
def newsitem(request,news_id):
    newssingle = Post.objects.get(id=news_id)
    alltag = tags.objects.all()
    c = {"news":newssingle,"tags":alltag}
    c.update(csrf(request))
    return render_to_response('news-single.htm', c)

def news(request):
    contact_list = Post.objects.all()
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    alltag = tags.objects.all()

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render_to_response('news.htm', {"news": contacts,"pages":paginator.count,"tags":alltag})