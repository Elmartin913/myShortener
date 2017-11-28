from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from analytics.models import ClickEvent

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
        # print(request.POST)
        # print(request.POST.get('url'))
        form = SubmitUrlForm(request.POST)
        context = {
            'title': 'Cutter site',
            'form': form,
        }
        template = 'cutter/home.html'
        if form.is_valid():
            print(form.cleaned_data.get('url'))
            new_url = form.cleaned_data.get('url')
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'create': created,
            }
            if created:
                template = 'cutter/succes.html'
            else:
                template = 'cutter/exists.html'

        return render(request, template, context)


class CutterRedirectView(View):  # class base view
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)

    # print(shortcode)
        #obj = get_object_or_404(ShortURL, shortcode=shortcode)


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
