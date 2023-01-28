from django.conf.urls import url
from dfr import views

urlpatterns = [
    url(r'^snippets/$', views.snipper_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_derail
]