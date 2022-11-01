# Generated by Django 4.1.2 on 2022-10-17 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BEAT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=100)),
                ('audio', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BEAT.usuario')),
            ],
        ),
    ]