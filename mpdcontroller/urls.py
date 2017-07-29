from django.conf.urls import url
import mpdcontroller.views as views

urlpatterns = [
  url(r'(?P<command>.+)/$', views.command),
  url(r'^$', views.controller, name='mpd_controller'),
]
