# Generated by Django 3.2.5 on 2021-11-14 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Name')),
                ('logo', models.CharField(max_length=150, verbose_name='Name')),
                ('url', models.CharField(max_length=150, verbose_name='URL')),
            ],
        ),
    ]
