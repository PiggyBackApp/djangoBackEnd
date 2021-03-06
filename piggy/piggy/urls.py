"""piggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# REST STUFF:
from rest_framework import routers
# VIEWS:
from posts import views as postsViews
from customUsers import views as customUsersViews

from rest_framework.authtoken import views as authViews

router = routers.DefaultRouter()
#makes sure that the API endpoints work
router.register(r'api/posts', postsViews.PostViewSet)
router.register(r'api/customUsers', customUsersViews.CustomUserViewSet)
router.register(r'api/requests', postsViews.RequestViewSet)
router.register(r'api/reviews', postsViews.ReviewViewSet)

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^authenticate/', customUsersViews.CustomObtainAuthToken.as_view()),
    url(r'^api-token-auth/', authViews.obtain_auth_token),
    url(r'^api/customUsers/', include('posts.urls', namespace='customUsers')),
    # url(r'^api/filter/q=(?P<query>.*)', include('posts.urls', namespace='customUsers')),
    # url(r'^api/filter/origin/q=(?P<origin_query>.*)', postsViews.PostViewSet),
    # url(r'^api/posts/origin/q=(?P<origin_query>.*)', postsViews.PostViewSet),
    url(r'^api/posts/', include('posts.urls', namespace='posts')),

]
