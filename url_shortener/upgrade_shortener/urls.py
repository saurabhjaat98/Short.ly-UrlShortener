from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name='main_home'),
    path('upgrade_plans/', views.Plans, name='Plans'),
    path('create/', views.UrlCreate, name='UrlCreate'),
    path('short.ly/<str:pk>', views.GoToDestinationUrl, name='destination'),
    path('delete/url/<str:pk>', views.DeleteUrl, name='deleteUrl'),
    path('edit/<str:pk>', views.EditUrl, name='EditUrl'),

]


