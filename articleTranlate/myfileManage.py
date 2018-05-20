#! python3
# -- coding: utf-8
import os
import codecs
import time
import datetime
import logging
import sys
from django.utils import timezone


# 传入英/汉 list 和保存文本的目录
# 创建的文本的文件名可以按时间创建
def toSaveTranlateArticle(translte_str_list, srcDir):
    logging.debug("toSaveTranlateArticle:")

    currTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
    fileNameEn = srcDir+"/en."+currTime
    fileNameZh = srcDir+"/zh."+currTime
    logging.debug(fileNameEn)
    logging.debug(fileNameZh)
    # print("fileNameEn:"+fileNameEn)
    # print("fileNameZh:"+fileNameZh)

    file1 = open(fileNameEn, 'w')
    # file1.write(text)        #写入内容信息
    file2 = open(fileNameZh, 'w')
    # file2.write(text)        #写入内容信息
    last_paragraph_id = 0

    curr_paragraph_id = 0


    for i in range(len(translte_str_list)):
        last_paragraph_id =  curr_paragraph_id
        curr_paragraph_id =  translte_str_list[i].paragraph_id

        

        if curr_paragraph_id != last_paragraph_id:
            file1.write("\n\n")  # 写入内容信息

        file1.write(translte_str_list[i].english_text)  # 写入内容信息
        
        if curr_paragraph_id != last_paragraph_id:
            file2.write("\n\n")  # 写入内容信息
        file2.write(translte_str_list[i].tranlate_text)  # 写入内容信息
        
    file1.close()

    file2.close()


# 检查当下需要生成文件所在的目录十分存在，不存在就创建，并返回目录地址
def checkFoldToSaveTranlate():

    # print("当前执行脚本的位置:"+sys.argv[0])#获得的是当前执行脚本的位置（若在命令行执行的该命令，则为空）
    # print("获得当前工作目录:"+os.getcwd())
    # print("获得当前工作目录:"+os.path.abspath('.'))
    # print("获得当前工作目录的父目录:"+os.path.abspath('..'))
    # print("获得当前工作目录:"+os.path.abspath(os.curdir))

    currTimeByDay = datetime.datetime.now().strftime('%Y-%m-%d')
    srcDir = os.getcwd()+"/src/"+currTimeByDay

    # print("srcDir:"+srcDir)

    if os.path.exists(srcDir) == True:
        pass
    else:
        os.makedirs(srcDir)
        print("checkFoldToSaveTranlate cre dir :"+srcDir)

    return srcDir


def main():

    logging.basicConfig(filename='example.log', level=logging.DEBUG)

    checkFoldToSaveTranlate()


# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == "__main__":
    main()
