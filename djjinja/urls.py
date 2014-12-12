
from django.conf.urls import patterns, url

from django.views.generic.base import TemplateView

from djjinja.views import Test1, Test2


urlpatterns = patterns('',
    url(r'^test1/$', Test1.as_view(), name='test-1'),
    url(r'^test2/$', Test2.as_view(), name='test-2'),
    #url(r'^test3/$', TemplateView.as_view(template_name='test3.jinja'), name='test-3')
)
