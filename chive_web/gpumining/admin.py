from django.contrib import admin
from .models import GPU, Order, OrderDetail
# Register your models here.
admin.site.register(GPU)
admin.site.register(OrderDetail)
admin.site.register(Order)
