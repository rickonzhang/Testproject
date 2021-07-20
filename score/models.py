from django.db import models

# Create your models here.
class Score(models.Model):
    class Meta:
        db_table = 'score'
        verbose_name = '分数表'
    s_id = models.IntegerField(null=True, default=None, verbose_name='学生号码')
    name = models.CharField(max_length=32, verbose_name='学生姓名')
    score = models.IntegerField(null=False, verbose_name='学生分数')
