from django.urls import path, include
from gpumining import views

from .viewsets import GPUViewset, OrderDetailViewset, OrderViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('gpus', GPUViewset)
router.register('orders', OrderViewset)
router.register('order_details', OrderDetailViewset)

urlpatterns = [
    path('gpumining', views.gpumining, name='gpumining'),
    path('api/', include(router.urls)),
]