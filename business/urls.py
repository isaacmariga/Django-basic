from django.urls import path, include
from . import views



urlpatterns = [
  path('', views.home,name = 'home'),
  path('business/<id>', views.batch,name = 'batch'),
  path('charts', views.charts,name = 'charts'),
]
