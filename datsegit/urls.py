from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from twhst.models import Hashtag
from datsegit.views import StatusFilteredList

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datsegit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^(P<hashtag>[^/]*)/(P<detail>[^/]*)', 'datsegit.views.hashtagDetail', name='hashtag_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(model=Hashtag, template_name="index.html"), name="homepage"),
    url(r'^(?P<slug>[^/]*)/(?P<letter>[a-zA-Z]+)', StatusFilteredList.as_view(), name='hashtag_letter'),
    url(r'^(?P<slug>[^/]*)$', DetailView.as_view(model=Hashtag, slug_field='name'), name='hashtag_index'),
)
