# Generated by Django 2.0.2 on 2020-02-19 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_ivent_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='kanmusu',
            name='ninki',
            field=models.IntegerField(default=0),
        ),
    ]
