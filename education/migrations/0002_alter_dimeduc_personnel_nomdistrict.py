# Generated by Django 4.1.6 on 2023-04-06 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimeduc_personnel',
            name='NomDistrict',
            field=models.CharField(max_length=250),
        ),
    ]
