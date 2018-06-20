#! python3
# -- coding: utf-8
import urllib.request
import urllib.parse
import json
import logging

import http.client
import hashlib
# import urllib
# import urllib.request.quote
from urllib import parse
import random


def youdaofanyi_api(content):   

    appKey = '311e65ddd97e13be'
    secretKey = '6BrsVRepP1XnPLGrYVizvwe77SbI6CVA'

    
    httpClient = None
    myurl = '/api'
    q = content
    fromLang = 'EN'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)

    sign = appKey+q+str(salt)+secretKey
    resStr ="NULL Str"
    # sign =hashlib.md5(sign).hexdigest()
    # 给中文
    sign = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()  

    # m1 = md5.new()
    # m1.update(sign)
    # sign = m1.hexdigest()
    myurl = myurl+'?appKey='+appKey+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = http.client.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
    
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        # print() 
        html = response.read().decode('utf-8')
        translate_results = json.loads(html)
        resStr = str(translate_results['translation'])

        resStr = resStr[2:len(resStr)-2]

        # print()

    except Exception as e:
        print(str(e))
        # print("Exception \n") 
    finally:
        if httpClient:
            httpClient.close()

    return resStr

def youdaofanyi_muti(content):   
    url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
    # http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    # http://fanyi.youdao.com/bbk/translate_m.do
    data={}
    data['i'] = "As it gains momentum, SD-WAN is disrupting the network purchasing decision, opening the market to new players and redefining networking itself."
    data['cache'] = 'true'
    data['tgt'] = "随着它的发展势头，它正在扰乱网络购买决策，向新玩家开放市场，并重新定义网络本身。"
    # data['i'] = line
    data['from'] = 'en'
    data['to'] = 'zh-CHS'
    # data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1528359243129'
    data['sign'] = 'fba1467ad053240ecbe20bc0577da6b2'
    data['doctype'] = 'json'
    data['version'] = '3.0'
    # data['keyfrom'] = 'fanyi.web'
    # data['action'] = 'FY_BY_CLICKBUTTION'
    # data['typoResult'] = 'false'
    strListByTrans =[]

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    print(str(html))
    print("\n\n") 
    translate_results = json.loads(html)
    # #######################################
    #找到翻译结果，load函数能将str转换成dict类型  现在是个字典了
    ############################################
    # translate_results = translate_results['translateResult'][0][0]['tgt']
    print("翻译：" +str(translate_results)+"\n\n") 
    translate_results = translate_results['translateResult']
    #打印翻译信息
    for i in translate_results:
         for j in i:
             for k in j:
                print("翻译的结果是："+k+" "  +j[k]) 
                strListByTrans.append(j[k])

    # print("翻译的结果是："  +translate_results) 
    return  strListByTrans




def youdaofanyi(content):      
    # 你可以对比下网页 https://blog.csdn.net/nunchakushuang/article/details/75294947
    # 里面的东西和这里代码的区别，看看思路是不是一样，总不能完全搞不懂原理

    # line = input('你想翻译啥:')
    # line = "IT’s path to digital transformation (DX) leadership is driven by IT’s organizational clout and ability to innovate. Does your IT group meet the criteria?'"
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
    data={}
    data['i'] = content
    # data['i'] = line
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1517799189818'
    data['sign'] = '8682192c0707c52ecdffbc98f77a17ac'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    strListByTrans =[]

    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    print(str(html))
    print("\n\n") 
    translate_results = json.loads(html)
    # #######################################
    #找到翻译结果，load函数能将str转换成dict类型  现在是个字典了
    ############################################
    # translate_results = translate_results['translateResult'][0][0]['tgt']
    print("翻译：" +str(translate_results)+"\n\n") 
    translate_results = translate_results['translateResult']
    #打印翻译信息
    for i in translate_results:
         for j in i:
             for k in j:
                print("翻译的结果是："+k+" "  +j[k]) 
                strListByTrans.append(j[k])

    # print("翻译的结果是："  +translate_results) 
    return  strListByTrans

def main():      

    logging.basicConfig(filename='example.log', level=logging.DEBUG)

          
    while 1:      
        content = input("输入待翻译内容：")    

        # logging.debug()
        logging.debug("input is："+content)
        if content == 'q!':  
            # 输入q!则终止循环
            # logging.debug("input is：q！")
            break      
        # tk = js.getTk(content)      
        # translate(content,tk)      
        # tmpstr = youdaofanyi(content)    
        tmpstr = youdaofanyi_api(content)    
        # print("翻译的结果是："  +tmpstr[1]) 

# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__ == "__main__":      
    main()   