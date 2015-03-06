from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'youlun.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'mixer.views.MixerView', name='Homepage mixer view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^json/(feeds|posts).json','ajaxApi.views.AjaxAPI'),
    url(r'^json/feeds/delete/(\d+)', 'ajaxApi.views.FeedDelete'),

)
