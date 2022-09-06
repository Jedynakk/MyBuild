# Generated by Django 4.1 on 2022-08-21 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0018_wydatki_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wydatki',
            name='kategoria',
            field=models.IntegerField(choices=[(1, 'materiały'), (2, 'narzedzia'), (3, 'pensje'), (4, 'podwykonawca'), (5, 'odpady'), (6, 'inne')], default=0),
        ),
    ]
