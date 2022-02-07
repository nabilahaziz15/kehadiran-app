# Generated by Django 2.2.21 on 2021-08-16 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hadir', '0004_hadir_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hadir',
            name='created_at',
        ),
        migrations.AddField(
            model_name='hadir',
            name='mac',
            field=models.CharField(default='34:97:F6:75:A1:AF', max_length=50),
        ),
        migrations.AlterField(
            model_name='hadir',
            name='city',
            field=models.CharField(default='Bogor', max_length=50),
        ),
        migrations.AlterField(
            model_name='hadir',
            name='lat',
            field=models.CharField(default='-6.597499847412109', max_length=50),
        ),
        migrations.AlterField(
            model_name='hadir',
            name='lng',
            field=models.CharField(default='106.78988647460938', max_length=50),
        ),
    ]