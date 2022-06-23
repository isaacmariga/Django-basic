from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
  path('', views.home,name = 'home'),
  path('new_batch', views.new_batch,name = 'new_batch'),
  path('new_customer', views.new_customer,name = 'new_customer'),
  path('new_expense', views.new_expense,name = 'new_expense'),
  path('new_revenue', views.new_revenue,name = 'new_revenue'),
  path('new_death', views.new_death,name = 'new_death'),
  path('business/<id>', views.batch,name = 'batch'),
  path('about/about', views.about,name = 'about'),
  path('landing/landing', views.landing,name = 'landing'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
