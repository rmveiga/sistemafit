# Generated by Django 3.0.7 on 2020-07-26 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acompanhamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acompanhamento',
            name='dt_medicao',
            field=models.DateField(verbose_name='Data de Medição'),
        ),
    ]
