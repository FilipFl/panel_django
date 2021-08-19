from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_view),
    path('prezent_dla_rudego', views.prezent_view),
    path('time_now', views.time_now),
]
