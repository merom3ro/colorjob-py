from django.urls import path

from . import colorjob

urlpatterns = [
    path('', colorjob.index, name='index'),
]