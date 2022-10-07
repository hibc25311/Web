from .models import GPU, OrderDetail, Order
from .serializers import GPUSerializer, OrderDetailSerializer, OrderSerializer
from rest_framework import viewsets


class GPUViewset(viewsets.ModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer


class OrderDetailViewset(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
