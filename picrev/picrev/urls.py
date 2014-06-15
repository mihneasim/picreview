from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from picrev.api import RequestResource

api = Api(api_name='v1')
api.register(RequestResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picrev.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api.urls)),
)
