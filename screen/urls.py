from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^getdevice', views.get_devices, name='getdevice'),
    url(r'^stfdevice', views.stf_deivce, name='rundevice'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),

]