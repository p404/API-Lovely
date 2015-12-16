from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^listings/$', views.listing_list),
    url(r'^listings/(?P<pk>[0-9]+)/$', views.listing_detail),
]
