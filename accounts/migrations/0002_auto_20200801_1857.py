# Generated by Django 3.0.8 on 2020-08-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_extend',
            name='ptr_join_yn',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
