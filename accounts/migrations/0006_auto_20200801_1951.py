# Generated by Django 3.0.8 on 2020-08-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200801_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_extend',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]
