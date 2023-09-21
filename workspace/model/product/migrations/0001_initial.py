# Generated by Django 4.2.3 on 2023-08-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField(default=0)),
                ('product_stock', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'tbl_product',
            },
        ),
    ]
