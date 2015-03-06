from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'mixer.views.MixerView', name='Homepage mixer view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^json/(feeds|posts).json' , 'ajaxApi.views.AjaxAPI'), #API Landing , returns FEEDS / POSTS.
    url(r'^json/feeds/delete/(\d+)', 'ajaxApi.views.FeedDelete'), #API Landing , deletes Feed from Mixer object.

)
