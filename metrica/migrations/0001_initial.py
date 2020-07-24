# Generated by Django 3.0.7 on 2020-07-24 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('unidade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metrica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('unidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='unidade.Unidade', verbose_name='Unidade')),
            ],
        ),
    ]
