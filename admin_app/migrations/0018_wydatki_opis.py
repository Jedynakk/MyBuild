# Generated by Django 4.1 on 2022-08-20 23:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0017_alter_wydatki_budowa'),
    ]

    operations = [
        migrations.AddField(
            model_name='wydatki',
            name='opis',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
