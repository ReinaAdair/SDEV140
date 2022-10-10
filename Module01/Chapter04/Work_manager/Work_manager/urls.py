'''from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url (r'^$', 'TasksManager.views.index.page'),
    url (r'^index$', 'TasksManager.views.index.page', name="public_index"),
    url (r'^connection$', 'TasksManager.views.connection.page', name="public_connection"),
)'''


#*** Deprecated, use below instead 10-2022 jtp *** from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
#from django.contrib import connections

admin.autodiscover()

from TasksManager.views.index import home
from TasksManager.views.index_for_templates import public_index
from TasksManager.views.connection import connections

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('index', public_index, name="public_index"),
    path('connections', connections, name="public_connections")
]