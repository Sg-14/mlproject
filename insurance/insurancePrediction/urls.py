from django.contrib import admin
from django.urls import path
from .views import predictView, predict
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', predictView, name='predictview'),
    path('predict', predict, name='predict')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)