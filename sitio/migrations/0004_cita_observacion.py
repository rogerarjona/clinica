# Generated by Django 2.1.5 on 2019-01-15 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0003_auto_20190114_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
