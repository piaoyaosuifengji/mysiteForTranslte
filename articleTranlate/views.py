#! python3
# -- coding: utf-8
import os
import codecs
import time
from django.shortcuts import get_list_or_404
# from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
# Create your views here.
from django.views import generic
from pyForTranslate.googleAPIForTranslate import googleAPIForTranslate, splitArticle 
from pyForTranslate.youdaofanyi import youdaofanyi,youdaofanyi_api
from .myfileManage import toSaveTranlateArticle, checkFoldToSaveTranlate
from .operatingdocx import CreTranslationDocx 

from pyForTranslate.HandleJs import Py4Js
import datetime
# from django.db import models
from django.utils import timezone
import random
import logging
from .models import translte_str
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect
import json
import requests
# import myfileManage

global translte_str_global
global english_text_global
global flag_for_get_translte_str
# global countTranlateStr_
# countTranlateStr_ =1

# 每刷新一次页面就会生成一个articleView 对象


class articleView_inputData():
    # listName
    # ArticleName
    def __init__(self, listName, ArticleName):
        self.listName = listName
        self.ArticleName = ArticleName


class articleView(generic.ListView):
    # 使用 template_name 来告诉 ListView 使用我们创建的已经存在的 "polls/index.html" 模板。
    template_name = 'articleTranlate/index.html'
    context_object_name = 'articleTranlate_list_name'
    # context_object_name2 = 'ArticleAddress_str_name'
    # count_ = 1

    def getTrranlateStrList(self):
        strListByTrans = googleAPIForTranslate("me")

        print("getTrranlateStrList  :")
        print(strListByTrans)
    # def __init__(self):
    #     # self.count_ = 1
    #     # logging.debug("__init__ ： here "+str(self.count_))
    #     translte_str_ = translte_str()
    #     translte_str_.english_text = timezone.now()
    #     translte_str_.tranlate_text = random.randint(0,99)
    #     translte_str_.save()

        # question = get_object_or_404(translte_str)

    # 这是因为logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，
    # 因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，
    # 而小于它的DEBUG和INFO级别的日志记录被丢弃了。
    # logging.debug("This is a debug log.")
    # logging.info("This is a info log.")
    # logging.warning("This is a warning log.")
    # logging.error("This is a error log.")
    # logging.critical("This is a critical log.")
    # printTranslate()

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]

        # translte_str_ = ["me","you"]
        # return translte_str.english_text

        translte_str_ = translte_str.objects.all()
        # translte_str.objects.
        # logging.debug("get_queryset count_ ： "+str(translte_str_.count()))

        return translte_str_
        # return translte_str.objects


@csrf_exempt
# @requires_csrf_token
def get_one_word(request):

    logging.debug("get_one_word : need to get_one_word:")
    english_text = ""
    ttranlate_text = ""

    # z这里需要js把需要翻译的word传回来阿，必须要post才行阿

    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        word_translate_ = request.POST.get('word_translate', '生生世世')
        # pwd_str=request.POST.get("pwd",'生生世世')
        logging.debug("word_translate:"+(word_translate_))
        # logging.debug("pwd_str:"+(pwd_str))
        strListByTrans = googleAPIForTranslate(word_translate_)
        for m in range(len(strListByTrans)):
            if m % 2 == 0:
                english_text = str(strListByTrans[m])
                ttranlate_text = str(strListByTrans[m+1])
                logging.debug("english_text:"+(english_text))
                logging.debug("ttranlate_text:"+(ttranlate_text))
              

    return HttpResponse(english_text+"："+ttranlate_text, content_type="text/plain")


def ajax_list(request):

    global translte_str_global
    global english_text_global
    global flag_for_get_translte_str

    if flag_for_get_translte_str == 1:

        name_dict = {'english_text': english_text_global,
                     'tranlate_text': translte_str_global}
        flag_for_get_translte_str = 0
        return JsonResponse(name_dict)

    else:
        pass
    flag_for_get_translte_str = 0

    # a = range(100)
    # return JsonResponse(a, safe=True)


def ajax_dict(request):
    logging.debug("ajax_dict : need to updata str is:")
    tranlate_text_ = request.POST['user']
    logging.debug("user ="+tranlate_text_)

    name_dict = {'twz': 'Love python and Django',
                 'zqxt': 'I am teaching Django1'}
    return JsonResponse(name_dict)


# 从网页获取文章的本地地址，并进行翻译后跳转到翻译显示界面
def getArticleAddress(request):
    logging.debug("getArticleAddress : ")
    ArticleAddress_str = None

    try:
        ArticleAddress_str = request.POST['articleAddress_str']  # 接收到的数据
    except Exception:
        logging.debug("getArticleAddress : Exception")

    context = {}
    if ArticleAddress_str == None:
        logging.debug("getArticleAddress : getArticleAddress is: none")
        context['ArticleAddress_str'] = 'none_'
    else:
        logging.debug(
            "getArticleAddress : getArticleAddress is:"+ArticleAddress_str)
        context['ArticleAddress_str'] = ArticleAddress_str

    # 如果得到的ArticleAddress_str是一个合法的地址
    # /home/jty/codetest/en.txt             ----测试文档
    if ArticleAddress_str != None:
        if os.path.exists(ArticleAddress_str) == True:
            logging.debug(
                "getArticleAddress : getArticleAddress can be open "+ArticleAddress_str)

            # 尝试打开文件
            # charCounts = os.path.getsize(ArticleAddress_str)   #zheg这个统计的字节数，而不是字符数
            # logging.debug("getArticleAddress : charCounts ： "+str(charCounts))
            #

            with codecs.open(ArticleAddress_str, "r", encoding="utf-8") as f:
                ArticleString = f.read()
            # print(text)
            # logging.debug("getArticleAddress : ArticleAddress_str ： \n"+ArticleString)

            # 先删除旧数据库
            translte_str_all = translte_str.objects.all()
            # translte_str.objects.all().delete()
            for tmpstr in translte_str_all:
                tmpstr.delete()

            # 这个列表中保存了所有的段落，包括标题，即每个list的对象是一个段落文本
            resultStr = splitArticle(ArticleString)
            # logging.debug("待翻译的段落：\n"+resultStr  )
          
            for i in range(len(resultStr)):
                if len(resultStr[i]) != 0:
                    # logging.info("len:"+str(len(resultStr[i])) + " " + resultStr[i])
                    # logging.info("\n\n下面是段落:"  +str(i) )

                    # 可以在这里进行翻译了
                    strListByTrans = googleAPIForTranslate(resultStr[i])

                    for m in range(len(strListByTrans)):
                        if m % 2 == 0:
                            # translte_str_obj =  translte_str(english_text=strListByTrans[m],tranlate_text=strListByTrans[m+1])
                            translte_str_obj = translte_str()

                            translte_str_obj.english_text = str(
                                strListByTrans[m])
                            translte_str_obj.tranlate_text = str(
                                strListByTrans[m+1])

                            tmp_translte_str = youdaofanyi_api(translte_str_obj.english_text)
                            translte_str_obj.tranlate_text_wy = tmp_translte_str

                            translte_str_obj.paragraph_id = i

                            translte_str_obj.save()
                            # logging.debug("english-----\n"+translte_str_obj.english_text)
                            # logging.debug("tranlate-----\n"+translte_str_obj.tranlate_text )

 
        else:
            logging.debug(
                "getArticleAddress : getArticleAddress can not be open "+ArticleAddress_str)

    return render(request, 'articleTranlate/getArticleAddress.html', context)


# 将数据库中的文本按一定格式写入到doc文件当中去
@csrf_exempt
def save_into_doc(request):

    last_paragraph_id = 0
    curr_paragraph_id = 0

    logging.debug("save_into_doc :   ")
    send_var = request.POST.get('send_var', '')
    # print(send_var)
    if send_var == "creDoc":
        logging.debug("save_into_doc :  order is： "+send_var)
        #  h获取 translte_str类型的在数据集中的所有对象
        translte_str_list = translte_str.objects.all()

        # 因为你之前保存的最终数据都是保存在 translte_str类的 变量 tranlate_text中的
        # 所以，你这里也只需要将这个变量中的数据保存到doc文件就行了
        if len(translte_str_list) > 0:
            creDoc = CreTranslationDocx("/home/jty/codetest","test.docx")
            # creDoc.add_heading( "标题")
            # creDoc.add_title("这句话的意思就是")
            # creDoc.add_sentence("话的意思就是，当模块被直接运行时，以下代码块将被运行", creDoc.add_paragraph())
            paragraph = ""

            for i in range(len(translte_str_list)):
                last_paragraph_id =  curr_paragraph_id
                curr_paragraph_id =  translte_str_list[i].paragraph_id

                #首先判断是不是文章的标题
                if curr_paragraph_id == last_paragraph_id:
                    if  last_paragraph_id == 0:
                        creDoc.add_heading( translte_str_list[i].tranlate_text)
                    else:
                        # 就是添加一个句子
                        creDoc.add_sentence(translte_str_list[i].tranlate_text, paragraph)
                else:
                    paragraph = creDoc.add_paragraph()
                    creDoc.add_sentence(translte_str_list[i].tranlate_text, paragraph)
                    # 还需要加入判断文章内部标题的判断，不太重要，暂时不管
                
            creDoc.save_()

    return HttpResponse("ok", content_type="text/plain")


# 功能和updataArticle相同，但是返回的是一个str：前端用js post
@csrf_exempt
def post_save_one_str(request):

    logging.debug("post_save_one_str : need to get_one_word:")
    english_text_ = ""
    tranlate_text_ = ""

    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        tranlate_text_ = request.POST.get('tranlate_text', '')
        english_text_ = request.POST.get('english_text', '')

        # 找到数据库里面english_text_的那个对象
        # translte_str_obj = get_object_or_404(
            # translte_str, english_text=request.POST['english_text'])

        translte_str_objs = get_list_or_404(translte_str, english_text=request.POST['english_text'])
        translte_str_obj = translte_str_objs[0]
        
        if tranlate_text_ == translte_str_obj.tranlate_text:
            logging.debug("english_text_ 不需要更新")
        else:
            translte_str_obj.tranlate_text = tranlate_text_
            translte_str_obj.save()
            logging.debug("tranlate_text_  更新为：" +translte_str_obj.tranlate_text)
            translte_str_all= translte_str.objects.all()

            # logging.debug(english_text_)
            # logging.debug(tranlate_text_)

            # 这里需要把更新后的内容同时保存一份，以文本的格式，到本地目录
            srcDir = checkFoldToSaveTranlate()
            logging.debug(srcDir)
            toSaveTranlateArticle(translte_str_all, srcDir)

    return HttpResponse("ok", content_type="text/plain")




# 暂时只能实现一次改一个句子
def updataArticle(request):
    logging.debug("updataArticle : need to updata str is:")

    translte_str_ = translte_str.objects.all()

    # english_text_ = request.POST['english_text']  # 接收到的数据
    tranlate_text_ = request.POST['tranlate_text']

    # 找到数据库里面english_text_的那个对象
    # get_object_or_404 会默认的调用django 的get方法， 如果查询的对象不存在的话，会抛出一个Http404的异常
    translte_str_obj = get_object_or_404(
        translte_str, english_text=request.POST['english_text'])

    # global translte_str_global
    # global english_text_global
    # global flag_for_get_translte_str

    # translte_str_global = tranlate_text_
    # english_text_global = english_text_
    # flag_for_get_translte_str = 1

    if translte_str_obj == None:
        return render(request, 'articleTranlate/index.html', {
            'translte_str': translte_str_,
            'error_message': "You can do nothing.",
        })

    else:
        context = {}
        context['articleTranlate_list_name'] = translte_str_
        if tranlate_text_ == translte_str_obj.tranlate_text:
            logging.debug("english_text_ 不需要更新")
        else:
            translte_str_obj.tranlate_text = tranlate_text_
            translte_str_obj.save()
            logging.debug("tranlate_text_  更新为：" +
                          translte_str_obj.tranlate_text)
            translte_str_ = translte_str.objects.all()
        # tranlate_text = request.POST['tranlate_text']下

        # logging.debug(english_text_)
        # logging.debug(tranlate_text_)

            # 这里需要把更新后的内容同时保存一份，以文本的格式，到本地目录
            srcDir = checkFoldToSaveTranlate()
            logging.debug(srcDir)
            toSaveTranlateArticle(translte_str_, srcDir)

            context['articleTranlate_list_name'] = translte_str_

        return render(request, 'articleTranlate/index.html', context)


 