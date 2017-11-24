from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ShortURL
from .forms import SubmitUrlForm
# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            'form': the_form,
            'title': 'Submit url: ',
        }
        return render(request, 'cutter/home.html', context)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(request.POST.get('url'))
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'cutter/home.html', {})


class CutterCBView(View):  # class base view
    def get(self, request, shortcode=None, *args, **kwargs):
        # print(shortcode)
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponse('hello again {}'.format(obj.url))

    def post(self, request, *arg, **kwargs):
        pass


# def cutter_fb_view(request, shortcode=None, *args, **kwargs):
    # print(shortcode)

    #obj = get_object_or_404(ShortURL, shortcode=shortcode)
    #obj_url = obj.url

    # try:
    #    obj = ShortURL.objects.get(shortcode=shortcode)
    # except:
    #    obj = ShortURL.objects.all().first()

    #obj_ulr = None
    #qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count() == 1:
    #    obj = qs.first()
    #    obj_url = obj.url
    # return HttpResponseRedirect(obj.url)
