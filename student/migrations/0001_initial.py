# Generated by Django 4.1 on 2023-09-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stuId', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('s1', models.CharField(max_length=10)),
                ('s2', models.CharField(max_length=10)),
                ('s3', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('speciality', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': '学生信息浏览',
                'verbose_name_plural': '学生信息表',
                'db_table': 'tb_student',
            },
        ),
    ]