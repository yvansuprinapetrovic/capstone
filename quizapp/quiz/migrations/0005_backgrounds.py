# Generated by Django 3.1.5 on 2021-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210429_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backgrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=200)),
            ],
        ),
    ]
