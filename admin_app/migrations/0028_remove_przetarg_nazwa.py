# Generated by Django 4.1 on 2022-08-28 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0027_tag_przetarg_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='przetarg',
            name='nazwa',
        ),
    ]