# Generated by Django 2.0.2 on 2020-06-08 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_auto_20200607_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='ido',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='battle',
            name='keido',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
