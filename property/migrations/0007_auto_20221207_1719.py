# Generated by Django 2.2.24 on 2022-12-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='_flat_liked_by_+', to='property.Flat', verbose_name='лайки'),
        ),
    ]