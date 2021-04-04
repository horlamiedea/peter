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
        return render(self.request, 'visitors.html')
    def post(self, *args, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('first_name')
            name_r = self.request.POST.get('last_name')
            email = self.request.POST.get('email')
            phone = self.request.POST.get('phone_number')
            address = self.request.POST.get('address')
            city = self.request.POST.get('city')
            state = self.request.POST.get('state')
            about = self.request.POST.get('about_you')
            
            collect = FirstTimer()
            collect.first_name = name
            collect.last_name = name_r
            collect.email = email
            collect.phone_number = phone
            collect.address = address
            collect.city = city
            collect.state = state
            collect.about_you = about
            collect.save()
            
            messages.success(self.request, f"Welcome to Our Church {name} {name_r}. We have appointed a host to you, The host will get accross to you very soon")
            return redirect('home')
        