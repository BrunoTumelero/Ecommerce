from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from client.adm_api import urls as adm_urls
from client.payment_api import urls as payment_urls

urlpatterns = [
    url(r'^adm/', include(adm_urls, namespace='adm')),
    url(r'^payment/', include(payment_urls, namespace='payment')),
]
