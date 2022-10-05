# *** Deprecated, use below instead 10-2022 jtp *** from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

admin.autodiscover()

from TasksManager.views.index import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home")
]