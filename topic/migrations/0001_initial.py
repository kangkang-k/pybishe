# Generated by Django 4.1 on 2023-09-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stuId', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('studentName', models.CharField(max_length=200)),
                ('teacherName', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.IntegerField()),
                ('teacherId', models.IntegerField()),
                ('topicFile', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'tb_topic',
            },
        ),
    ]