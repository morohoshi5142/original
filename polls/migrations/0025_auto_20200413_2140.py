# Generated by Django 2.0.2 on 2020-04-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20200413_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playquestion',
            name='question_text',
            field=models.TextField(verbose_name='本文'),
        ),
    ]
