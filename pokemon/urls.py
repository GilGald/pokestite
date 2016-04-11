from django.conf.urls import url

from . import views

urlpatterns = [    
    url(r'^(?P<q>\w+)/$', views.index, name='index'),
]