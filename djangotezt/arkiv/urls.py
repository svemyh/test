from django.urls import path

from . import views
from .views import index1

urlpatterns = [
    path('', index1, name="yes"),
    #path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),

    # ex: /arkiv/5/
    path('<int:item_id>/', views.detail, name='detail'),
    # ex: /arkiv/5/name/
    path('<int:item_id>/name/', views.name, name='name'),
    # ex: /arkiv/5/physical_id/
    path('<int:item_id>/physical_id/', views.physical_id, name='physical_id'),
]