# Generated by Django 4.1.1 on 2022-10-23 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BEAT', '0002_cancion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cancion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='edad',
        ),
    ]