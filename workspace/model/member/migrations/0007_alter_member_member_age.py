# Generated by Django 4.2.3 on 2023-08-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_member_member_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_age',
            field=models.PositiveSmallIntegerField(default='1'),
        ),
    ]
