# Generated by Django 3.0.6 on 2020-05-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0002_auto_20200505_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(default='', max_length=200),
        ),
    ]
