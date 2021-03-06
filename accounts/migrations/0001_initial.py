# Generated by Django 3.0.8 on 2020-07-29 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_extend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=15)),
                ('prof_img', models.ImageField(null=True, upload_to='profile')),
                ('ptr_join_yn', models.CharField(max_length=1)),
                ('biz_nm', models.CharField(max_length=200, null=True)),
                ('actv_area', models.CharField(max_length=100)),
                ('svc_cd', models.CharField(max_length=6)),
                ('work_spc_kind', models.CharField(max_length=20)),
                ('career', models.IntegerField(null=True)),
                ('lic_img', models.ImageField(null=True, upload_to='license')),
                ('staff_cnt', models.IntegerField(null=True)),
                ('user_type', models.CharField(max_length=1, null=True)),
                ('del_yn', models.CharField(default='N', max_length=1, null=True)),
                ('del_res', models.CharField(max_length=200, null=True)),
                ('reg_dtti', models.DateTimeField(auto_now_add=True)),
                ('mod_dtti', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
