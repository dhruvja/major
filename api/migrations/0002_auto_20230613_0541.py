# Generated by Django 3.2.16 on 2023-06-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultupload',
            name='error',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='resultupload',
            name='loading',
            field=models.BooleanField(default=False),
        ),
    ]
