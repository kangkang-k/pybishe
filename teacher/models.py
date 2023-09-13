from django.db import models


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    clzz = models.CharField(max_length=300)

    class Meta:
        db_table = 'tb_teacher'
