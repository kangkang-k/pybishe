from django.db import models


#  签到统计表
class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    late = models.CharField(max_length=100)
    late_time = models.CharField(max_length=100)
    create_time = models.CharField(max_length=100)
    signIn = models.CharField(max_length=100)

    '''自定义表名,默认表名'''

    class Meta:
        db_table = 'tb_attendance'
        verbose_name = '签到统计表'
        verbose_name_plural = "签到统计表"

    def __str__(self):
        return self.__dict__
