from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.template import loader
from datetime import datetime

# Create your views here.
def bot_view(request):
    return render(request, 'bot/basic.html',
                  {
                      'days': '30',
                      'date': timezone.now().date,
                  })