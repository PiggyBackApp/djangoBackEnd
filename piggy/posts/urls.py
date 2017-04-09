from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<reviewee>\d+)/reviews/$',
        views.ListCreateReview.as_view(),
        name='review_list'),
    url(r'^(?P<reviewee>\d+)/reviews/(?P<pk>\d+)/$',
        views.RetrieveUpdateDestroyReview.as_view(),
        name='review_detail'),
]
