# Generated by Django 4.1 on 2022-08-19 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_przetarg_budzet_alter_budowa_budzet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='przetarg',
            name='data',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
