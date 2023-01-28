from django.conf.urls import url
from dfr import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^snippets/$', views.snipper_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_derail),
]

urlpatterns = format_suffix_patterns(urlpatterns)