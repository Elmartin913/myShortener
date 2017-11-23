from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShortURL
# Create your views here.


def cutter_fb_view(request, shortcode=None, *args, **kwargs):
    # print(shortcode)

    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    obj_url = obj.url

    # try:
    #    obj = ShortURL.objects.get(shortcode=shortcode)
    # except:
    #    obj = ShortURL.objects.all().first()

    #obj_ulr = None
    #qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count() == 1:
    #    obj = qs.first()
    #    obj_url = obj.url

    return HttpResponseRedirect(obj.url)


class CutterCBView(View):  # class base view
    def get(self, request, shortcode=None, *args, **kwargs):
        # print(shortcode)
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponse('hello again {}'.format(obj.url))

    def post(self, request, *arg, **kwargs):
        pass
