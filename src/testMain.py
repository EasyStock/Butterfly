# coding=utf-8
'''
@Date: 2020-04-26 23:22:36
@LastEditTime: 2020-05-09 12:29:48
@Author: yuchonghuang@sina.cn
'''
import tests

import requests

def TestGetTHS():
    payload = {'Accept': 'application/json, text/javascript, /; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                #'Cookie': 'PHPSESSID=a586067bc69c163c04f0c38169a23d70;',
                #'cid': 'a586067bc69c163c04f0c38169a23d701588926227;',
                #'ComputerID': 'a586067bc69c163c04f0c38169a23d701588926227; WafStatus=0; guideState=1; v=AjRtT-iB1tFdvUIdZhTez-YBA_mlDVhomjDsOs6VwnRCZdov9h0oh-pBvM0d',
                'hexin-v': 'AjRtT-iB1tFdvUIdZhTez-YBA_mlDVhomjDsOs6VwnRCZdov9h0oh-pBvM0d',
                'Host': 'www.iwencai.com',
                'Referer': 'http://www.iwencai.com/stockpick/search?typed=0&preParams=&ts=1&f=1&qs=1&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=%E5%BC%80%E7%9B%98%E4%BB%B7%EF%BC%8C+%E6%94%B6%E7%9B%98%E4%BB%B7%EF%BC%8C%E6%9C%80%E9%AB%98%E4%BB%B7%EF%BC%8C%E6%9C%80%E4%BD%8E%E4%BB%B7',
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
                'X-Requested-With':'XMLHttpRequest', 
                 }
    r = requests.get('http://www.iwencai.com/stockpick/load-data?typed=0&preParams=&ts=1&f=1&qs=result_original&selfsectsn=&querytype=stock&searchfilter=&tid=stockpick&w=%E5%BC%80%E7%9B%98%E4%BB%B7%EF%BC%8C+%E6%94%B6%E7%9B%98%E4%BB%B7%EF%BC%8C%E6%9C%80%E9%AB%98%E4%BB%B7%EF%BC%8C%E6%9C%80%E4%BD%8E%E4%BB%B7&queryarea=',headers = payload)
    js = r.json()
    print(js['data']['result']['result'])
    print(js['data']['result']['token'])
    print(js['data']['result']['total'])
    print(js['data']['result']['perpage'])
    print(js['data']['result']['page'])

    url = 'http://x.iwencai.com/stockpick/cache?token=%s'%(js['data']['result']['token'])
    url = url + '&p=3&perpage=1000&showType=[%22%22,%22%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22,%22onTable%22]'
    s = requests.get(url,headers = payload)
    js1= s.json()  
    print(js1)  
    
    

if __name__ == "__main__":
    TestGetTHS()