# Generated by Django 2.0.2 on 2020-02-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_kanmusu_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='ivent',
            name='pub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
