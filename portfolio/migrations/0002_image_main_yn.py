# Generated by Django 3.0.8 on 2020-07-31 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='main_yn',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
