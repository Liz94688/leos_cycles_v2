# Generated by Django 3.1.2 on 2020-11-08 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0003_auto_20201108_1822'),
        ('bike', '0002_auto_20201108_1822'),
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.bike')),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.calendarevent')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.order')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.services')),
            ],
            options={
                'verbose_name_plural': 'OrderLineItem',
            },
        ),
    ]