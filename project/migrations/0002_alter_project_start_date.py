# Generated by Django 4.1.2 on 2022-10-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]