from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('7<str:pk>', views.GoToMainUrl, name='GoToMainUrl'),
    path('delete/<str:pk>', views.deleteUrl, name='deleteShortUrl'),
    path('', include('upgrade_shortener.urls')),

]
