# Generated by Django 2.2.17 on 2021-03-22 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IOTD', '0006_remove_vote_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-likes']},
        ),
    ]
