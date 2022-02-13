from django.shortcuts import render
from .models import Card_Model, Blog_Model
  
# Create your views here.
def index(request):
      
    # render function takes argument  - request
    # and return HTML as response
    card = Card_Model.objects.all()
    return render(request, "index.html", {'card' : card})

def blog_page(request, slug):
    blog = Blog_Model.objects.get(slug = slug)
    card = Card_Model.objects.get(slug = slug)
    context = {
        "blog" : blog,
        "card": card,
    }
    return render(request, "blog.html", context=context)