from django.shortcuts import render
from .models import Card_Model
  
# Create your views here.
def index(request):
      
    # render function takes argument  - request
    # and return HTML as response
    card = Card_Model.objects.all()
    return render(request, "index.html", {'card' : card})
