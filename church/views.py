from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Event, New, Sermon , Contact, FirstTimer
from . forms import  VisitorForm
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

class Home(View):
    def get(self, request, *args, **kwargs):
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
    
    
    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            name_r = self.request.POST.get('name')
            email_r = self.request.POST.get('email')
            message_r = self.request.POST.get('message')

            c = Contact(name=name_r, email=email_r, message=message_r)
            c.save()
            messages.success(self.request, "Your message has been sent successfully, Please wait while we get back to you")
            return redirect('home')
    


# def sermon(request):
#     sam = Sermon.objects.all()
#     return render(request, 'sermons.html')

class SermonView(ListView):
    model = Sermon
    template_name = 'sermons.html'
    
    
class EventView(ListView):
    model = Event
    template_name = 'events.html'
    
# def visit(request):
#     return render(request, 'visitors.html')
    
    
class VisitorView(View):
    def get(self, *args, **kwargs):
        form =  VisitorForm()
        context = {
            'form': form
        }
        return render(self.request, 'visitors.html', context)