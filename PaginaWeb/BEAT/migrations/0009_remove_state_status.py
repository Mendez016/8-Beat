# Generated by Django 4.1.2 on 2022-11-02 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BEAT', '0008_state_pku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='status',
        ),
    ]
