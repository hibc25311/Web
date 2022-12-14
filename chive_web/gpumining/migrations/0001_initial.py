# Generated by Django 3.2.12 on 2022-10-07 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=10)),
                ('price', models.IntegerField(blank=True)),
                ('algo', models.CharField(max_length=10)),
                ('hashrate', models.FloatField(null=True)),
                ('profit', models.FloatField(null=True)),
                ('power', models.IntegerField(null=True)),
                ('img_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(null=True)),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpumining.gpu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gpumining.order')),
            ],
            options={
                'unique_together': {('gpu', 'order')},
            },
        ),
        migrations.AddField(
            model_name='order',
            name='gpus',
            field=models.ManyToManyField(through='gpumining.OrderDetail', to='gpumining.GPU'),
        ),
    ]
