from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_view),
    path('prezent_dla_rudego', views.prezent_view),
    path('time_now', views.time_now),
    path('prezent_dla_rudego_ready', views.ready_view),
    path('find_sum_parts', views.find_sum_parts, name='find_sum_parts'),
    path('find_parts', views.find_sum_parts_form, name='find_parts'),
]
