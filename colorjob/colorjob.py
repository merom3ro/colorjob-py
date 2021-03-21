import os

from django.http import HttpResponse, JsonResponse
from colorthief import ColorThief
from urllib import request
import itertools

cont = itertools.count()

def index(_request):
    print(_request.headers)
    fname = str.format("img{}.png", next(cont))
    request.urlretrieve(
        _request.headers['Imgurl'],
        fname)
    thief = ColorThief(fname)
    palette = thief.get_palette(color_count=6, quality=6)
    os.remove(fname)
    return JsonResponse({'palette': palette})
