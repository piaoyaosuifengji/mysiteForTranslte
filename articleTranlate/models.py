#! python3
# -- coding: utf-8
from django.db import models
import datetime
# from django.db import models
from django.utils import timezone
# Create your models here.

class translte_str(models.Model):

    # 定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。
    # Django 支持所有常用的数据库关系：多对一、多对多和一对一。
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)

    english_text = models.CharField(max_length=5500)
    tranlate_text = models.CharField(max_length=5500)
    tranlate_text_wy = models.CharField(max_length=5500, default='nulll')

    # id =  models.IntegerField(default=0)#当断失断
    paragraph_id = models.IntegerField(default=0)
    # def __str__(self):
    #         return self.choice_text