# Generated by Django 3.2 on 2022-03-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='balance_gr',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='first_num',
            field=models.IntegerField(),
        ),
    ]