from django.shortcuts import render

from .models import Card_Model, Blog_Model

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from .form import ContactForm

  
# Create your views here.
def index(request):
    # render function takes argument  - request
    # and return HTML as response
    if request.method == 'POST':
        task = ContactForm(request.POST or None)
        if task.is_valid():
            task.save()
            return HttpResponse("Thanks for Subscribing! Yor Are Now Family")
        else:
            return HttpResponse('OOps!! Invalid Email Address')
    else :
        card = Card_Model.objects.all().order_by('-id')        # All Card Objects
        paginator = Paginator(card, 10, orphans=1)          # Per Page Card
        page_number = request.GET.get('page')           # Holds Current Page number Value
        page_obj = paginator.get_page(page_number)          # Renders that page whose value is passed
        return render(request, "index.html", {'card' : page_obj})
        

def blog_page(request, slug):
    blog = Blog_Model.objects.get(slug = slug)
    card = Card_Model.objects.get(slug = slug)
    context = {
        "blog" : blog,
        "card": card,
    }
    return render(request, "blog.html", context=context)

def home(request):
    if request.method == 'POST':
        task = ContactForm(request.POST or None)
        if task.is_valid():
            task.save()
            return HttpResponse("We are Contact as soon as Possible")
        else:
            return HttpResponse('Please try Again later, something went wrong')
        return redirect('welcome')


