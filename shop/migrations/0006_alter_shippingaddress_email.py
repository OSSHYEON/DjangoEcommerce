# Generated by Django 4.0.1 on 2022-02-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_shippingaddress_total_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
