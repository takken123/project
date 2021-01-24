# Generated by Django 3.0.7 on 2021-01-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]