from django.db import models


#  管理员
class MyAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    create_time = models.CharField(max_length=100)
    update_time = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)

    '''自定义表名,默认表名'''

    class Meta:
        db_table = 'tb_admin'
        verbose_name = '管理员'
        verbose_name_plural = "管理员"

    def __str__(self):
        return self.__dict__
