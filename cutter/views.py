from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


def cutter_fb_view(request, *args, **kwargs):
    return HttpResponse('Hello')


class CutterCBView(View):  # class base view
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello again')
