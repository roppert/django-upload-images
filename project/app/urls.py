from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^gallery/(?P<id>\d+)/$', views.gallery, name="gallery"),
    url(r'^image/$', views.image, name="image"),
    url(r'^image/(?P<id>\d+)/$', views.image, name="image"),
]
