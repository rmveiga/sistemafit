# Generated by Django 3.0.7 on 2020-07-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidade', '0003_auto_20200725_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidade',
            name='digitos',
            field=models.IntegerField(default=0, verbose_name='Dígitos'),
        ),
    ]
