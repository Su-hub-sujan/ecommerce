
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='shop-home'),
    path('about/',views.about,name='about'),
    path('contact/',views.about,name='contact'),
    path('checkout/',views.about,name='check'),
    path('productview/',views.productview,name='prod'),

    path('search/',views.search,name='search'),
    path('tracker/',views.tracker,name='tracker'),
]