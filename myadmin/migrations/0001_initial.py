# Generated by Django 4.1 on 2023-09-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('create_time', models.CharField(max_length=100)),
                ('update_time', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
                'db_table': 'tb_admin',
            },
        ),
    ]