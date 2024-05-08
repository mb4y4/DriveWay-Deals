# Generated by Django 3.0.7 on 2024-05-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20240312_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='car_photo_1',
        ),
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Kisumu', 'Kisumu'), ('Nakuru', 'Nakuru'), ('Eldoret', 'Eldoret'), ('Thika', 'Thika'), ('Malindi', 'Malindi'), ('Kitale', 'Kitale'), ('Garissa', 'Garissa'), ('Kakamega', 'Kakamega'), ('Nyeri', 'Nyeri'), ('Meru', 'Meru'), ('Lamu', 'Lamu'), ('Kericho', 'Kericho'), ('Machakos', 'Machakos'), ('Naivasha', 'Naivasha'), ('Embu', 'Embu'), ('Kisii', 'Kisii'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Nyahururu', 'Nyahururu'), ('Voi', 'Voi'), ('Nanyuki', 'Nanyuki'), ('Isiolo', 'Isiolo'), ('Mandera', 'Mandera'), ('Homa Bay', 'Homa Bay'), ('Lodwar', 'Lodwar'), ('Wajir', 'Wajir'), ('Migori', 'Migori'), ('Kitui', 'Kitui'), ('Marsabit', 'Marsabit'), ('Kilifi', 'Kilifi'), ('Bondo', 'Bondo'), ('Webuye', 'Webuye'), ('Kerugoya', 'Kerugoya'), ('Bomet', 'Bomet'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Maralal', 'Maralal'), ('Ruiru', 'Ruiru'), ('Lugulu', 'Lugulu'), ('Mbale', 'Mbale'), ('Taveta', 'Taveta'), ('Oyugis', 'Oyugis')], max_length=100),
        ),
    ]