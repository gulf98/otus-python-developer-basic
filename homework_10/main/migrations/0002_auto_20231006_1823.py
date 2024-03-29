# Generated by Django 3.2 on 2023-10-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'ordering': ['pk'], 'verbose_name': 'Zoo animal', 'verbose_name_plural': 'Zoo animals'},
        ),
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Name'),
        ),
    ]
