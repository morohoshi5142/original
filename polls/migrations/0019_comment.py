# Generated by Django 2.0.2 on 2020-04-06 13:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20200318_2206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='名無し', max_length=255, verbose_name='名前')),
                ('text', models.TextField(verbose_name='本文')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Playnikki', verbose_name='対象記事')),
            ],
        ),
    ]
