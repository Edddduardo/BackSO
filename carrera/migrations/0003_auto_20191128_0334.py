# Generated by Django 2.2.7 on 2019-11-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrera', '0002_auto_20191128_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='director',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
