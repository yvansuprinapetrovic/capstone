# Generated by Django 3.1.5 on 2021-04-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='number',
            field=models.CharField(max_length=1000),
        ),
    ]