from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from twhst.models import Hashtag
from datsegit.views import StatusFilteredList, DictionaryListView, HashtagDetailView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ListView.as_view(model=Hashtag, template_name="index.html"), name="homepage"),
    url(r'^(?P<slug>[^/]+)/(?P<word>[-\w]{2,})', DictionaryListView.as_view(), name='dictionary_item'),
    url(r'^(?P<slug>[^/]+)/(?P<letter>[a-z]{1})', StatusFilteredList.as_view(), name='hashtag_letter'),
    url(r'^(?P<slug>[^/]+)$', HashtagDetailView.as_view(slug_field='name'), name='hashtag_index'),
)
