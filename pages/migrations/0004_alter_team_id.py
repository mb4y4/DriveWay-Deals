# Generated by Django 3.2 on 2024-05-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20240508_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]