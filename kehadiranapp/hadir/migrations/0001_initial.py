# Generated by Django 2.0.4 on 2021-03-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hadir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.CharField(max_length=50)),
                ('lokasi', models.CharField(max_length=50)),
            ],
        ),
    ]
