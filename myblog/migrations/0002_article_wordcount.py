# Generated by Django 2.0.6 on 2018-06-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='wordcount',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
