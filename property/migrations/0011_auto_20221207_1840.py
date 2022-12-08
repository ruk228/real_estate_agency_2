# Generated by Django 2.2.24 on 2022-12-07 14:47
import phonenumbers

from django.db import migrations


def normalization_number(apps, Flat):
    Flat = apps.get_model('property', 'Flat')
    print(2)
    for flat in Flat.objects.filter(owners_phonenumber='+70000000000'):

        owners_phonenumber = flat.owners_phonenumber
        phone_number = phonenumbers.parse(owners_phonenumber, 'RU')

        if phonenumbers.is_valid_number(phone_number):
            flat.owner_pure_phone = None
        else:
            flat.owner_pure_phone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)

        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20221207_1839'),
    ]

    operations = [
        migrations.RunPython(normalization_number)
    ]
