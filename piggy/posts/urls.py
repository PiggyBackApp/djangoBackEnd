from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<reviewee>\d+)/reviews/$',
        views.ListCreateReview.as_view(),
        name='review_list'),
    url(r'^(?P<reviewee>\d+)/reviews/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyReview.as_view(),
        name='review_detail'),
    url(r'^$', views.PostViewSet, name='post_list'),
    url(r'^origin/q=(?P<origin_query>.*)/$', views.ListCreateOriginPost.as_view()),
    url(r'^destination/q=(?P<destination_query>.*)/$', views.ListCreateDestinationPost.as_view()),
    url(r'^both/q=(?P<origin_query>.*)/q=(?P<destination_query>.*)/$', views.ListCreateBothPost.as_view()),
    url(r'^self/$', views.OwnPostsViewSet, name='post_list'),


]
