# Generated by Django 3.0.8 on 2020-08-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200801_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_extend',
            name='nickname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user_extend',
            name='svc_cd',
            field=models.CharField(max_length=20),
        ),
    ]