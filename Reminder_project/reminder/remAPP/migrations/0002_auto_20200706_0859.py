# Generated by Django 2.2.5 on 2020-07-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder_mod',
            name='date',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='reminder_mod',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
