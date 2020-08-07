# Generated by Django 3.0.8 on 2020-08-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0003_auto_20200807_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='req_area',
        ),
        migrations.AddField(
            model_name='request',
            name='area_sido',
            field=models.CharField(default='서울특별시', max_length=50),
        ),
        migrations.AddField(
            model_name='request',
            name='area_sigungu',
            field=models.CharField(default='강남구', max_length=50),
        ),
    ]
