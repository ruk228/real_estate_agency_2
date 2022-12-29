# Generated by Django 2.2.24 on 2022-12-09 14:32

from django.db import migrations
from property.models import Owner


def transfer(apps, Flat):

    Flat = apps.get_model('property', 'Flat')

    for falt in Flat.objects.all():

        Owner.objects.get_or_create(
            owner_name=falt.owner,
            owner_pure_phone=falt.owner_pure_phone,
            owners_phonenumber=falt.owners_phonenumber,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20221221_1909'),
    ]

    operations = [
        migrations.RunPython(transfer)
    ]



