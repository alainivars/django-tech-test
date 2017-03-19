from django.conf.urls import url, include
from django.contrib import admin
from . import views

from views import ContactFormView


urlpatterns = [
    url(r'^contact/$', ContactFormView.as_view(), name='contact'),
    url(r'^success/$', views.success, name='success'),
    # url(r'^admin/', include(admin.site.urls)),
]