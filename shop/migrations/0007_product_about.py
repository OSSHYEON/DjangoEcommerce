# Generated by Django 4.0.1 on 2022-02-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_shippingaddress_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.TextField(blank=True, null=True),
        ),
    ]
