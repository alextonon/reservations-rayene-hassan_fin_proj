# Generated by Django 4.2.11 on 2024-04-25 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservationhub', '0003_client_passager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='utilisateur',
            new_name='utilisateur_reservation',
        ),
    ]
