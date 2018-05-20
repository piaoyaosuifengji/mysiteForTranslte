# -- coding: utf-8
#!/usr/bin/python3
import sys
import os
import re
# from hcdn_mainwin import *
import time
import logging
import urllib.request      
from pyForTranslate.HandleJs import Py4Js 
#获取系统时间，如果超过固定时间就退出

# timeStr=time.strftime('%Y-%m',time.localtime(time.time()))
# print(timeStr)
ys=time.strftime('%Y',time.localtime(time.time()))
ms=time.strftime('%m',time.localtime(time.time()))


# print(timeStr)
# ys,ms=time.localtime(time.time())

ysD=int(ys)
msD=int(ms)
# print(ysD)
# print(msD)
if ysD >2018 or msD > 6:
    sys.exit(0)
else:
    pass

# main_win()



# 需要建立两种进程
#     1：主进程，一个，负责字典数据读取和md5计算结果的最终确认
#     2：md5计算进程，多个




def printTranslate():
    print ("printTranslate")
    logging.debug("printTranslate")

    # return  print ("printTranslate")


def open_url(url):      

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}    

    #  The default is 'GET' if data is None     # 
    req = urllib.request.Request(url = url,headers=headers)   


    # response是一个 HTTPResposne 类型的对象，它主要包含的方法有 read() 、 readinto() 、getheader(name) 、 getheaders() 、 fileno() 等函数
    # 和 msg 、 version 、 status 、 reason 、 debuglevel 、 closed 等属性   
    response = urllib.request.urlopen(req)   

    # 但是得到了response并不代表得到了我们想要的网页数据,只能得到包头信息,只有当实现read  
    # 方法时才会从服务器请求到数据包的正文内容
    # 返回的是html字符串类型。
    data = response.read().decode('utf-8')    
    # logging.debug("\n data type is ："+ str(print(type(data)) ) )
    
    return data      
      
def translate(content,tk):      
    # strlen_=len(content)
    # logging.debug("strlen_ is："+str(strlen_))
    # logging.debug("-----："+content)
    strListByTrans =[]
    if len(content) > 4891:      
        print("翻译的长度超过限制！！！")      
        return     
    countTmp = 0  
    '''
    URL中的字符只能是ASCII字符，但是ASCII字符比较少，而URL则常常包含ASCII字符集以外的字符，
    如非英语字符、汉字、特殊符号等等，所以要对URL进行转换。这个过程就叫做URL编码，或者叫URL转义，
    实质上就是将包含非ASCII字符的URL转换为有效的ASCII字符格式。
    '''
    content = urllib.parse.quote(content)      
        #   https://translate.google.cn/?hl=zh-CN
    url = "http://translate.google.cn/translate_a/single?client=t"+ "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"+"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"+"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)      
          
    #返回值是一个多层嵌套列表的字符串形式，解析起来还相当费劲，写了几个正则，发现也很不理想，    
    #后来感觉，使用正则简直就是把简单的事情复杂化，这里直接切片就Ok了     
    # 显然，这里返回的就是翻译后的所以内容了，但是不仅仅是翻译，还有其他的信息 
    result = open_url(url)      
    # logging.debug("\ntranslate  result  is ：" )
    # logging.debug(result)
    '''
    str.find(str, beg=0, end=len(string))
    检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
    如果包含子字符串返回开始的索引值，
    否则返回-1。

    '''
    end = result.find("\",")      # 查找是否有  “，   的字符串，这里找的是第一句翻译的末尾的 “，
    # endOfStr = result.find(r"\[\[")
    if end > 4:      
        # print("找到组数：",end)      
        # print(result[4:end])   #result[4:end]的意思是，返回第四个字符到第end个字符之间的这个字符串
        
        # 在这里进行终极字符串的分割，算法参见文本
        # 谷歌翻译字符串解析文本.txt
        '''
        步骤：
            1：去掉第一个[
            2：找到第一个  ]]的地方，就是包含了所以翻译的字符串文本（有多余部分）

            3：去掉头尾的[]
            4：开始按照  ],   分割字符串,以下面的例子为例，会分割成4个字符串，
                更好的方法是：找寻字符串  ],  找到一个就意味着找到了一个翻译对
            5：对每个翻译对进行进一步的提取---就是最终结果      
        '''
        # 1和2。3
        endOfStr = result.find(r"]]")
        totalStr =result[1:endOfStr+2]
        # print("endOfStr",str(endOfStr))
        # print("totalStr：",totalStr)    

        while len(totalStr) > 2:
            endOfStr = totalStr.find(r"],")
            if endOfStr != -1:
                # 4
                singleSentenceStr = totalStr[0:endOfStr+1]
                # print("singleSentenceStr",singleSentenceStr)

                # 5 对每个翻译    进行进一步的提取---就是最终结果  
                end = singleSentenceStr.find("\",")    
                if countTmp == 0:
                    strForTranlate = singleSentenceStr[3:end]
                else:
                    strForTranlate = singleSentenceStr[2:end]   

                countTmp=countTmp+1
                # strForTranlate = singleSentenceStr[2:end]
                # print("strForTranlate",strForTranlate)

                singleSentenceStr =singleSentenceStr[end+3:-1]

                end = singleSentenceStr.find("\",")       
                strForEnglish = singleSentenceStr[0:end]
                # print("strForEnglish",strForEnglish)
                strListByTrans.append(strForEnglish)
                strListByTrans.append(strForTranlate)

                totalStr = totalStr[endOfStr+2:-1]
            else:
                break
            


    return strListByTrans

#这个函数用来将整个文本分割成一段段的段落文本
# 显然，在linux utf8编码下，段落的分割换行靠的是一个： 0a  （实际上可能有多个0a）


# 条件：
# 1：utf8编码、
# 2：文件的第一行，以0a 开头，就是说第一行为空
# 3：文件的最后一行，以0a 结尾

def splitArticle(Article_str):
    # Article_str中就是整个文档
    # 那就是解析成段落后保存与一个列表中进行数据返回
    # 只能用列表


    resultStr = re.split('\n(.+)\n', Article_str,re.M)
    resultStr2 = []
    # j =0
    # logging.debug("\n")
    # logging.debug("splitArticle：")

    # logging.debug("len is："+str(len(resultStr) ) )
    for i in range(len(resultStr)):
    #  print ("序号：%s   值：%s" % (i + 1, list[i]))
        # 要除去字符串中开头结尾的换行符号
        resultStr[i].rstrip('\n')
        resultStr[i].rstrip()
        resultStr[i].lstrip('\n')
        resultStr[i].lstrip()

        countOfN = resultStr[i].count('\n')
        if len(resultStr[i]) != 0 and len(resultStr[i]) != countOfN:
            # resultStr.pop(i)
            # logging.debug("len:"+str(len(resultStr[i])) + " "+ resultStr[i])
            resultStr2.append(resultStr[i])

    # logging.debug("end of splitArticle\n")

    # for i in list:
        # print ("序号：%s   值：%s" % (list.index(i) + 1, i))
    return resultStr2

# //传入的是一段落需要翻译的中文文本，返回该段落按句子分割开的一个list（英文文本在前，中文文本在后）
def googleAPIForTranslate(strNeedToTranslate): 
    js = Py4Js()      
          
   
    # 计算tk的值，暂时不管
    tk = js.getTk(strNeedToTranslate)  

    # 把需要翻译的文本和翻译文本都放在一起
    strListByTrans = translate(strNeedToTranslate,tk)   


    return strListByTrans



def main():      
    # 参考：
    # https://blog.csdn.net/yingshukun/article/details/53470424
    # https://blog.csdn.net/andeyeluguo/article/details/78581590
    # github地址：https://github.com/cocoa520/Google_TK
    # 
    # 
    logging.basicConfig(filename='example.log', level=logging.DEBUG)

    js = Py4Js()      
          
    while 1:      
        content = input("输入待翻译内容：")    

        # logging.debug()
        logging.debug("input is："+content)
        if content == 'q!':  
            # 输入q!则终止循环
            # logging.debug("input is：q！")
            break      
        # 计算tk的值，暂时不管
        tk = js.getTk(content)      
        translate(content,tk)      
          

# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == "__main__":      
    main()   