from django.db import models


class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    stuId = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    studentName = models.CharField(max_length=200)
    teacherName = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField()  # 0 未提交,1已提交,待审核, 1审核通过 2 打回
    teacherId = models.IntegerField()
    topicFile = models.CharField(max_length=500)

    '''自定义表名,默认表名'''

    class Meta:
        db_table = 'tb_topic'

    def __str__(self):
        return self.__dict__
