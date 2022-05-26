from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index0(request):
    template_name = 'homepage/index.html'
    template_name = 'homepage/layout.html'
    return render(request, template_name)
