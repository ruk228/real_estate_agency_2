# Generated by Django 2.2.24 on 2022-12-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='_flat_liked_by_+', to='property.Flat', verbose_name='лайки'),
        ),
    ]
