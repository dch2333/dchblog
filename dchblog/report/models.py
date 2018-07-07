from django.db import models
from django.utils import timezone

# Create your models here.


class Form(models.Model):
    date = models.DateTimeField(default=timezone.now)  # 时间
    myclass = models.CharField(max_length=20)  # 专业班级
    name = models.CharField(max_length=10)  # 姓名
    reason_in_school = models.CharField(
        max_length=100, blank=True)  # 校内晚归原因、地点
    reason_out_school = models.CharField(
        max_length=100, blank=True)  # 校外晚归原因、地点
    return_time = models.CharField(
        max_length=20, blank=True)  # 返校时间
    tell = models.CharField(max_length=11)  # 联系电话
    connect = models.CharField(max_length=5)  # 是否能联系上
    another_tell = models.CharField(max_length=11)  # 所在宿舍联系人电话
    fudaoyuan = models.CharField(max_length=10)  # 辅导员

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-date',)
        verbose_name = "零汇报"
        verbose_name_plural = "零汇报"
