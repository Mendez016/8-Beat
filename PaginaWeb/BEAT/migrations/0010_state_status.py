# Generated by Django 4.1.2 on 2022-11-02 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEAT', '0009_remove_state_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='status',
            field=models.CharField(default='n', max_length=2),
            preserve_default=False,
        ),
    ]
