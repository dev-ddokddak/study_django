# Generated by Django 4.2.4 on 2023-08-04 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='update_date',
            new_name='updated_date',
        ),
    ]
