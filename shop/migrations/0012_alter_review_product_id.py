# Generated by Django 4.0.1 on 2022-02-11 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_review_product_review_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product'),
        ),
    ]
