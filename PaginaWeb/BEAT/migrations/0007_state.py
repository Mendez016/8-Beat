# Generated by Django 4.1.2 on 2022-11-01 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEAT', '0006_rename_audioprim_cancion_prim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=2)),
            ],
        ),
    ]
