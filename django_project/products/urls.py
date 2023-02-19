from django.urls import path
from django.conf.urls import url
from .views import ProductView


urlpatterns = [
        # url for search 
        url('search/', ProductView.as_view(),  name='product-search'),

]