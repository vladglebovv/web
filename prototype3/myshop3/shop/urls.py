from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^products/decor', views.product_list_decor, name='product_list_decor'),
    url(r'^products/decor/vases', views.product_list_decor_vase, name='product_list_decor_vase'),
    url(r'^products/tableware', views.product_list_tableware, name='product_list_tableware'),
    url(r'^products/chancellery', views.product_list_chancellery, name='product_list_chancellery'),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^show_orders/$', views.show_orders, name='show_orders'),
]