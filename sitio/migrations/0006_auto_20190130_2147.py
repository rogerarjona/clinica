# Generated by Django 2.1.5 on 2019-01-31 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0005_auto_20190130_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='dia_agendado',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora_agendado',
            field=models.TimeField(null=True),
        ),
    ]