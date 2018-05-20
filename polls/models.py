#! python3
# -- coding: utf-8
import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
            return self.question_text
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):

    # 定义了一个关系。这将告诉 Django，每个 Choice 对象都关联到一个 Question 对象。
    # Django 支持所有常用的数据库关系：多对一、多对多和一对一。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
            return self.choice_text
"""
    每个字段都是 Field 类的实例 - 比如，
    字符字段被表示为 CharField ，
    日期时间字段被表示为 DateTimeField 。这将告诉 Django 每个字段要处理的数据类型。

    每个 Field 类实例变量的名字（例如 question_text 或 pub_date ）也是字段名
        数据库会将它们作为列名。


    你可以使用可选的选项来为 Field 定义一个人类可读的名字。
    这个功能在很多 Django 内部组成部分中都被使用了，而且作为文档的一部分。
    在上面的例子中，我们只为 Question.pub_date 定义了对人类友好的名字。  

"""         

