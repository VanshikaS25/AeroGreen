# Generated by Django 4.2.1 on 2023-05-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aerodevs', '0005_product_part_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='part_id',
            field=models.IntegerField(default=0),
        ),
    ]
