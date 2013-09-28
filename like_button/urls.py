from django.conf.urls.defaults import *
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^channel.html$', TemplateView.as_view(), {
        'template': 'channel.html'}),
)
