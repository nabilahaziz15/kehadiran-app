# Generated by Django 2.2.21 on 2021-12-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadir', '0012_auto_20211203_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hadir',
            name='lat',
            field=models.CharField(default='-6.246437233432436', max_length=50),
        ),
        migrations.AlterField(
            model_name='hadir',
            name='lng',
            field=models.CharField(default='106.86762789979684', max_length=50),
        ),
    ]