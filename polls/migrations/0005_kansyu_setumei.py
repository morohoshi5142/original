# Generated by Django 2.0.2 on 2020-01-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_sanka_kanmusu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kansyu_setumei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setumei', models.CharField(max_length=200)),
            ],
        ),
    ]
