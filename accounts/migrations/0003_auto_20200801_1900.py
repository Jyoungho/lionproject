# Generated by Django 3.0.8 on 2020-08-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200801_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_extend',
            name='ptr_join_yn',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='user_extend',
            name='user_type',
            field=models.CharField(max_length=1),
        ),
    ]
