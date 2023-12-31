# Generated by Django 4.2.4 on 2023-08-03 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('seq_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'sequence',
            },
        ),
    ]
