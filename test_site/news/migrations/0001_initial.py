# Generated by Django 3.1.4 on 2020-12-12 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meldung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('zeitstempel', models.DateTimeField()),
                ('text', models.TextField(verbose_name='Meldungstext')),
            ],
        ),
        migrations.CreateModel(
            name='Kommentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=70)),
                ('text', models.TextField(verbose_name='Kommentartext')),
                ('meldung', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.meldung')),
            ],
        ),
    ]
