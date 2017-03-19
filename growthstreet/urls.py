from django.conf.urls import include, url
from django.contrib import admin

from borrow import urls as borrow_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^borrow/', include(borrow_urls))
]
