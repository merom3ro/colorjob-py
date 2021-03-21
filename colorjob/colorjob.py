import os

from django.http import HttpResponse, JsonResponse
from colorthief import ColorThief
import itertools

from colorjob.forms import UploadFileForm

cont = itertools.count()

def index(_request):
    print(_request)
    print(_request.FILES)
    print(_request.headers)

    if _request.method == 'POST':
        form = UploadFileForm(_request.POST, _request.FILES)
        if form.is_valid():
            thief = ColorThief(_request.FILES['file'])
            palette = thief.get_palette(color_count=6, quality=6)
            print(palette)
            return JsonResponse({'palette': palette})
    return HttpResponse('non-valid request')

