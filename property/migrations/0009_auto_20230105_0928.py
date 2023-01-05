# Generated by Django 2.2.24 on 2023-01-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_remove_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(choices=[('NEW_BUILDING', 'Новостройка'), ('OLD_BUILDING', 'Cтарое здание'), ('UNKNOWN', 'Неизвестно')], db_index=True, default='UNKNOWN', null=True, verbose_name='Статус постройки здания'),
        ),
    ]
