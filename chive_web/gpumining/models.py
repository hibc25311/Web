from django.db import models


# Create your models here.
class GPU(models.Model):

    model = models.CharField(max_length=20)
    brand = models.CharField(max_length=10)
    price = models.IntegerField(blank=True)
    algo = models.CharField(max_length=10)
    hashrate = models.FloatField(null=True)
    profit = models.FloatField(null=True)
    power = models.IntegerField(null=True)
    img_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.model


class Order(models.Model):
    email = models.EmailField(max_length=40, unique=True)
    gpus = models.ManyToManyField(GPU, through='OrderDetail')

    def __str__(self):
        return self.email


class OrderDetail(models.Model):

    gpu = models.ForeignKey(GPU, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    qty = models.IntegerField(null=True)

    class Meta:
        unique_together = (('gpu', 'order'), )

    def __str__(self):
        return f'{self.order.email}, {self.gpu}, {self.qty}'
