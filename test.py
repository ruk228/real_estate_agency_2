# Generated by Django 2.2.24 on 2022-12-09 14:32

from django.db import migrations


def transfer(apps, Owner, Flat):

    Flat = apps.get_model('Propety', 'Flat')
    Owner = apps.get_model('Propety', 'Owner')

    for falt in Flat.objects.all():

        Owner.objects.get_or_create(
            name=falt.owner,
            owner_pure_phone=falt.owner_pure_phone,
            owners_phonenumber=falt.owners_phonenumber,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_owner'),
    ]

    operations = [
        migrations.RunPython(transfer)
    ]



















# Generated by Django 2.2.24 on 2022-12-07 14:47
import phonenumbers

from django.db import migrations


def normalization_number(apps, Flat):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():

        owners_phonenumber = flat.owners_phonenumber
        phone_number = phonenumbers.parse(owners_phonenumber, 'RU')

        if phonenumbers.is_possible_number(phone_number):
            flat.owner_pure_phone = owners_phonenumber
        else:
            flat.owner_pure_phone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)

        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20221207_1719'),
    ]

    operations = [
        migrations.RunPython(normalization_number)
    ]




from django.db import migrations


def change_building_status(apps, Flat):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():

        if 2014 < flat.construction_year:
            flat.new_building = True
            flat.save()
            #Flat.objects.update_or_create(owner=flat.owner,
            #                            price=flat.price,
            #                            new_building=True,
            #                            rooms_number=flat.rooms_number,
            #                            active=flat.active)
        else:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(change_building_status),
    ]


x = phonenumbers.parse("+79022185804", 'RU')
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
'+79022185804'
>>> phonenumbers.is_possible_number(x)
True
