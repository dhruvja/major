# Generated by Django 3.2.16 on 2023-01-25 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default=2023, max_length=255)),
                ('on_campus', models.IntegerField(default=0)),
                ('off_campus', models.IntegerField(default=0)),
                ('internship', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=255)),
                ('batch', models.CharField(choices=[('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], default=2023, max_length=255)),
                ('without_backlog', models.IntegerField(default=0)),
                ('single_backlog', models.IntegerField(default=0)),
                ('double_backlog', models.IntegerField(default=0)),
                ('triple_backlog', models.IntegerField(default=0)),
                ('more_than_3_backlog', models.IntegerField(default=0)),
                ('dropouts', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='admission',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('3', '3')], max_length=255),
        ),
        migrations.CreateModel(
            name='ResultFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result', to='api.result')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('placement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placement', to='api.placement')),
            ],
        ),
    ]
