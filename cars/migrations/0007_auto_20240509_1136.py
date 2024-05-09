# Generated by Django 3.0.7 on 2024-05-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20240509_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('MSA', 'Mombasa'), ('KWA', 'Kwale'), ('KIL', 'Kilifi'), ('TAN', 'Tana River'), ('LAM', 'Lamu'), ('TAI', 'Taita/Taveta'), ('GAR', 'Garissa'), ('WAJ', 'Wajir'), ('MAN', 'Mandera'), ('MAR', 'Marsabit'), ('ISR', 'Isiolo'), ('MER', 'Meru'), ('THA', 'Tharaka-Nithi'), ('EMB', 'Embu'), ('KIT', 'Kitui'), ('MAC', 'Machakos'), ('MAK', 'Makueni'), ('NYN', 'Nyandarua'), ('NYE', 'Nyeri'), ('KIR', 'Kirinyaga'), ('MUR', "Murang'a"), ('KIA', 'Kiambu'), ('TUR', 'Turkana'), ('WPO', 'West Pokot'), ('SAM', 'Samburu'), ('TNZ', 'Trans Nzoia'), ('UGI', 'Uasin Gishu'), ('EMK', 'Elgeyo/Marakwet'), ('NAN', 'Nandi'), ('BAR', 'Baringo'), ('LAI', 'Laikipia'), ('NAK', 'Nakuru'), ('NAR', 'Narok'), ('KAJ', 'Kajiado'), ('KER', 'Kericho'), ('BOM', 'Bomet'), ('KAK', 'Kakamega'), ('VIH', 'Vihiga'), ('BUN', 'Bungoma'), ('BUS', 'Busia'), ('SIA', 'Siaya'), ('KIS', 'Kisumu'), ('HOM', 'Homa Bay'), ('MIG', 'Migori'), ('KIS', 'Kisii'), ('NYA', 'Nyamira'), ('NBO', 'Nairobi City')], max_length=100),
        ),
    ]
