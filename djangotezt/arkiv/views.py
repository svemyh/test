from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
#from models import Item



# Create your views here.
def index1(request):
    
    c1 = 'polls/index.html'
    c2 = 'polls/arkiv3.html'
    return render(request, c2)


def detail(request, item_id):
    return HttpResponse("You're looking at question %s." % item_id)

def name(request, item_id):
    response = "You're looking at the name of item with id: %s."
    return HttpResponse(response % item_id)

def physical_id(request, item_id):
    return HttpResponse("You're looking at the physical id of item with id: %s." % item_id)


