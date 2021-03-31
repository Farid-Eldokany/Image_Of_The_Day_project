# Generated by Django 2.2.17 on 2021-03-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IOTD', '0017_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('image_id', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=128)),
                ('reason', models.CharField(max_length=128)),
            ],
        ),
    ]
