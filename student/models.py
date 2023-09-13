from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    stuId = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    s1 = models.CharField(max_length=10)
    s2 = models.CharField(max_length=10)
    s3 = models.CharField(max_length=10)
    college = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)

    '''自定义表名,默认表名'''

    class Meta:
        db_table = 'tb_student'
        verbose_name = '学生信息浏览'
        verbose_name_plural = "学生信息表"

    def __str__(self):
        return self.__dict__
