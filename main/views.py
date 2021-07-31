from django.shortcuts import render
from django.http import HttpResponse

def basic_view(request):
    #return render(request, 'about_me.html')
    return HttpResponse('Nothing to see here...')


def prezent_view(request):
    return render(request, 'prezent.html')
