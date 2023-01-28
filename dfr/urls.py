from django.conf.urls import url
from dfr import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dfr.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers


snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^snippets/$', snippet_list, name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
    url(r'users/$', user_list, name='user-list'),
    url(r'users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')


])


from django.conf.urls import url, include
from dfr import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# urlpatterns = format_suffix_patterns([
#
#     path('', views.api_root),
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')
#
#     # path('user/', views.UserList.as_view()),
#     # path('users/<int:pk>/', views.UserDetail.as_view()),
#     # path('', views.api_root),
#     # path('snippets/<int:pk>/highlight', views.SnippetHighlight)
# ])

# urlpatterns = format_suffix_patterns(urlpatterns)