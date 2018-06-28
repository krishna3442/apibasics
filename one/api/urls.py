from .views import BlogPostRudView,BlogPostApiView
from django.conf.urls import url


app_name= 'one'


urlpatterns = [
    url(r'^$',BlogPostApiView.as_view(),name='one-create'),
    url(r'^(?P<pk>\d+)$',BlogPostRudView.as_view(),name='one-rud'),
]
