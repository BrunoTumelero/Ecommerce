from django.urls import re_path

from .views import *

app_name ="core"

urlpatterns = [
    re_path(r'^get_products/(?P<pk>\d+)$', get_products, name='get_all_products'),
    re_path(r'^get_products$', get_products, name='get_products'),   
]