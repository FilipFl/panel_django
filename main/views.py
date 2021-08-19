import datetime

from django.shortcuts import render
from django.http import HttpResponse

def basic_view(request):
    #return render(request, 'about_me.html')
    return HttpResponse('Nothing to see here...')


def prezent_view(request):
    return render(request, 'prezent.html')

def time_now(request):
    return HttpResponse(str(datetime.datetime.now()))
    #return render(request, 'prezent2.html')