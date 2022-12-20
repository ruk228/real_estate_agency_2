# Generated by Django 2.2.24 on 2022-12-09 14:32

from django.db import migrations
from property.models import Owner


def fill_owners(apps, schema_editor):

    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    #test1 = Flat.objects.filter(address=falt.address)


    instance = Owner.objects.create(name=Flat)
    print(instance)


    for test in instance:
        instance.apartment_owner.set(test.address)



def transfer(apps, Flat):#

    Flat = apps.get_model('property', 'Flat')

    for falt in Flat.objects.all():

        #if not Owner.objects.filter(name=falt.owner).exists():

        owner = Owner.objects.create(apartment_owner=falt.address)
        owner.emails_for_help.set()
        #owner.save()
            #apartment_owner='57330'#falt.address,

        break


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20221209_2214'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]
