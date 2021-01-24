# Generated by Django 3.0.7 on 2021-01-23 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_detail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_detail',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('delivered', 'Delivered')], default='draft', max_length=10),
        ),
    ]
