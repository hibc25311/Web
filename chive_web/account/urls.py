from django.urls import path
from account import views

urlpatterns = [
    path('sign-up', views.sign_up, name='sign-up'),
    path('test', views.test, name='test'),
]
