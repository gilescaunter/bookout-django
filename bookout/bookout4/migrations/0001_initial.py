# Generated by Django 2.0.1 on 2018-01-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logsheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pilot', models.CharField(max_length=255)),
                ('logDate', models.DateField()),
                ('logTime', models.CharField(max_length=5)),
                ('logFrom', models.CharField(max_length=30)),
                ('logTo', models.CharField(max_length=30)),
                ('logAircraftType', models.CharField(max_length=20)),
                ('logAircraftReg', models.CharField(max_length=20)),
                ('logPax', models.IntegerField(default=1)),
                ('logDorA', models.CharField(max_length=1)),
                ('logEntryDatetime', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pilots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('aircraftType', models.CharField(max_length=20)),
                ('aircraftReg', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
