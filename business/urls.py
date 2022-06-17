from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
  path('', views.home,name = 'home'),
  path('new_batch', views.new_batch,name = 'new_batch'),
  path('business/<id>', views.batch,name = 'batch'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
