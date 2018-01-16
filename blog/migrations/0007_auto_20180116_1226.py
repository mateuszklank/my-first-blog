# Generated by Django 2.0.1 on 2018-01-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_lekarz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lekarz',
            old_name='imie',
            new_name='imię',
        ),
        migrations.AlterField(
            model_name='lekarz',
            name='specjalizacja',
            field=models.CharField(choices=[('CH', 'Chirurg'), ('NC', 'Neurochirurg'), ('KG', 'Kardiolog'), ('AN', 'Anestezjolog'), ('EN', 'Endokrynolog')], default='CH', max_length=2),
        ),
    ]
