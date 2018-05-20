#! python3
# -- coding: utf-8

from django.contrib import admin

# Register your models here.

from .models import Question,Choice

# admin.site.register(Question)
 

# class QuestionAdmin(admin.ModelAdmin):
#     # fields = ['pub_date', 'question_text']
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Choice)



# 这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)