from django.urls import path, include
from API_app import views

urlpatterns = [
    path('index/', views.index),
    path('generic/', views.generic),
    path('elements/', views.elements),
    path('map/', views.map),
    path('map2/', views.map2),
    path('test_enter/', views.enter),

]