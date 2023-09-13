from django.db import models


#  专升本学生
class UpgradeStudent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stuId = models.CharField(max_length=100)
    upgrade_time = models.CharField(max_length=100)
    create_time = models.CharField(max_length=100)
    update_time = models.CharField(max_length=100)

    '''自定义表名,默认表名'''

    class Meta:
        db_table = 'upgrade_student'
        verbose_name = '专升本学生'
        verbose_name_plural = "专升本学生"

    def __str__(self):
        return self.__dict__
