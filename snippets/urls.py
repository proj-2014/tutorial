
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

'''
# for views.py
urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)
'''

'''
# for views2.py
urlpatterns = patterns('snippets.views2',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)


urlpatterns = format_suffix_patterns(urlpatterns)
'''

#for views3.py

from snippets import views3 

urlpatterns = patterns('',
    url(r'^snippets/$', views3.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views3.SnippetDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)

