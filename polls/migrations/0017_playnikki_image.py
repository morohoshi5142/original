# Generated by Django 2.0.2 on 2020-03-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20200311_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='playnikki',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]