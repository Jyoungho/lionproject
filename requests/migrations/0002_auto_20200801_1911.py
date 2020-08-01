# Generated by Django 3.0.8 on 2020-08-01 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='img',
        ),
        migrations.CreateModel(
            name='Request_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='requests')),
                ('main_yn', models.CharField(default='N', max_length=1)),
                ('req_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.Request')),
            ],
        ),
    ]
