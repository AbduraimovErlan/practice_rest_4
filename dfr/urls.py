from django.conf.urls import url
from dfr import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail')




    # path('user/', views.UserList.as_view()),
    # path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('', views.api_root),
    # path('snippets/<int:pk>/highlight', views.SnippetHighlight)
])

# urlpatterns = format_suffix_patterns(urlpatterns)