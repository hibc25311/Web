from rest_framework import serializers
from .models import GPU, Order, OrderDetail


class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = ['id', 'model', 'brand', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'email', 'gpus']


class OrderDetailSerializer(serializers.ModelSerializer):
    order = serializers.SlugRelatedField(slug_field='email',
                                         queryset=Order.objects.all())

    # gpu_model = serializers.ReadOnlyField(source='gpu.model')
    # order_email = serializers.ReadOnlyField(source='order.email')

    class Meta:
        model = OrderDetail
        fields = ['id', 'gpu', 'order', 'qty']
