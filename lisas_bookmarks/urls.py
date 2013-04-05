from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf.urls.defaults import*

from django.contrib.auth.models import User

from project.views import*

urlpatterns = patterns('',

    #Browsing
    (r'^$', 'main_page'),
    (r'^user/(\w+)/$', 'user_page'),
     #Examples:
     #url(r'^$', 'lisas_bookmarks.views.home', name='home'),
     #url(r'^lisas_bookmarks/', include('lisas_bookmarks.foo.urls')),

     
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #I uncommented the line below, it said to put django.contrib.admin into INSTALLED_APPS in settings 
    #url(r'^admin/', include(admin.site.urls)),
)



#urlpatterns=patterns('', (r'^$', main_page),)

