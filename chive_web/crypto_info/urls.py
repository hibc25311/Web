from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coin', views.coin, name='coin'),
    path('news', views.news, name='news'),
]