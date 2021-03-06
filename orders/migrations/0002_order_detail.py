# Generated by Django 3.0.7 on 2021-01-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('order_id', models.IntegerField()),
                ('price', models.IntegerField()),
                ('firstname', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
