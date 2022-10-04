# *** Deprecated, use below instead 10-2022 jtp *** from django.conf.urls import include, url
from django.urls import include, re_path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # *** url is deprecated as of 1.6. using re_path instead - 10-2022 jtp ***
    # url(r'^$', 'Work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    re_path(r'^admin/', admin.site.urls),

    # from page 25 in book
    # re_path(r'^$', 'TasksManager.views.index.page'), 
    # re_path(r'^index$', 'TasksManager.views.index.page') 
]