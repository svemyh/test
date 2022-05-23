from django.urls import path

from . import views
from .views import index0

urlpatterns = [
    path('', index0),
    #path('', views.index, name='index'),
]
