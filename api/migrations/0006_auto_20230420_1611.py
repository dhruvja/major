# Generated by Django 3.2.16 on 2023-04-20 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20230420_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='batch',
            new_name='admission_year',
        ),
        migrations.RenameField(
            model_name='placement',
            old_name='batch',
            new_name='admission_year',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='batch',
            new_name='admission_year',
        ),
    ]