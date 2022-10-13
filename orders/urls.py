from django.urls import path

from orders.views import index, get_order, admin, accept

urlpatterns = [
    path("",index, name="index"),
    path("www/",admin, name="admin"),
    path("accept/",accept, name="accept"),
    path("get_order/",get_order, name="get_order"),
]