# Generated by Django 4.2.7 on 2023-11-07 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webscraper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joblisting',
            name='company',
        ),
    ]
