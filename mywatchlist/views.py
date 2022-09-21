from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_mywatchlist_msg(request):
    data_watchlist = MyWatchList.objects.all()
    watched_status = (data_watchlist.filter(watched = True)).count() >= (data_watchlist.filter(watched = False)).count()

    context = {
        'data_mywatchlist': data_watchlist,
        'nama': 'Davyn Reinhard Santoso',
        'kelas': 'PBP - C',
        'student_id': 2106751083,
        'watched_status' : 
                'Selamat, kamu sudah banyak menonton!' if watched_status 
                else 'Wah, kamu masih sedikit menonton!',
    }
    return render(request, 'mywatchlist.html',context)


def show_mywatchlist_html(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'data_mywatchlist': data_watchlist,
        'nama': 'Davyn Reinhard Santoso',
        'kelas': 'PBP - C',
        'student_id': 2106751083,
    }
    return render(request, 'mywatchlist.html', context)

def show_watchlist_xml(request):
    data_watchlist= MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data_watchlist), content_type="application/xml")

def show_watchlist_json(request):
    data_watchlist= MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data_watchlist), content_type="application/json")
