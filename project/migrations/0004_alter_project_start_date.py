# Generated by Django 4.1.2 on 2022-10-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
    ]
