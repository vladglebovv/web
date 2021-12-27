from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^products/bath', views.product_list_bath, name='product_list_bath'),
    url(r'^products/sink', views.product_list_sink, name='product_list_sink'),
    url(r'^products/tap', views.product_list_tap, name='product_list_tap'),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^show_orders/$', views.show_orders, name='show_orders'),
]