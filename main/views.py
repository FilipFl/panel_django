import datetime

from django.shortcuts import render
from django.http import HttpResponse

def basic_view(request):
    #return render(request, 'about_me.html')
    return HttpResponse('Nothing to see here...')

def prezent_view(request):
    return render(request, 'prezent2.html')

def ready_view(request):
    new_day = datetime.datetime(2021, 8, 20, 22, 00, tzinfo=None)
    if datetime.datetime.now() < new_day:
        return render(request, 'oszust.html')
    return render(request, 'prezent_lokacja.html')

def time_now(request):
    new_day = datetime.datetime(2021, 8, 19, 15, 30, tzinfo=None)

    return HttpResponse(str(datetime.datetime.now() > new_day))
    #return render(request, 'prezent2.html')