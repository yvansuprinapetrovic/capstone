# Generated by Django 3.1.5 on 2021-04-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.CharField(default=None, max_length=2000),
        ),
    ]
