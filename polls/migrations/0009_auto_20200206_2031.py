# Generated by Django 2.0.2 on 2020-02-06 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_ivent_tokkokanmusu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ivent_naiyou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naiyou', models.CharField(max_length=200)),
                ('ivent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Ivent')),
            ],
        ),
        migrations.RemoveField(
            model_name='tokkokanmusu',
            name='ivent',
        ),
        migrations.AddField(
            model_name='tokkokanmusu',
            name='ivent_naiyou',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Ivent_naiyou'),
            preserve_default=False,
        ),
    ]
