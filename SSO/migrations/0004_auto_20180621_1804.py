# Generated by Django 2.0.6 on 2018-06-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSO', '0003_auto_20180621_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
