from django.conf.urls import patterns, include, url
from django.views.generic import DetailView
from twhst.models import Hashtag

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datsegit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^(P<hashtag>[^/]*)/(P<detail>[^/]*)', 'datsegit.views.hashtagDetail', name='hashtag_detail'),
    url(r'^(?P<slug>[^/]*)$', DetailView.as_view(model=Hashtag, slug_field='name'), name='hashtag_index'),
    url(r'^admin/', include(admin.site.urls)),
)
