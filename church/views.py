from django.shortcuts import render
from django.views.generic import View
from .models import Event, New, Sermon
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'index.html')

class Home(View):
    def get(self, *args, **kwargs):
        sermon = Sermon.objects.all()
        paginator = Paginator(sermon, 4)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        event = Event.objects.all()
        pag = Paginator(event, 4)
        pag_number = self.request.GET.get('page')
        pag_obj = paginator.get_page(pag_number)
        new = New.objects.all()
        pags = Paginator(new, 4)
        pags_number = self.request.GET.get('page')
        pags_obj = pags.get_page(pags_number)
        context = {
            'page_obj': page_obj,
            'pag_obj': pag_obj,
            'pags_obj': pags_obj
        }
        return render(self.request, 'index.html', context)