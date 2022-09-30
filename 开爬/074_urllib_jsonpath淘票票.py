# _*_ coding:utf-8 _*_
# @Time : 2022/9/30 14:50
# @Author : fx
# @File : 074_urllib_jsonpath淘票票
# @Project : pythonProject

import json
import jsonpath
import urllib.request

# 注意请求的是不是具体的城市，而是选择框allCity
url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1664521706296_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?city=110100&_ksTS=1664520670476_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cookie': 't=f3d084eaab841373ff83df1f7187e1c3; cna=lg0fGx3aLGICAd9bEzOyLCSS; cookie2=19eed1ce017d41ef33820012be879e70; v=0; _tb_token_=fea83834e3635; tb_city=110100; tb_cityName="sbG+qQ=="; isg=BPb2HnaniXctFX2Q7S3_ee9HRyz4FzpRdA0Hv2DewFl0o5U9yKYhYeoSu3_PCzJp; l=eBgOmZWrT_ccT6TpBO5ZKurza779FIOf1sPzaNbMiInca6iRtFtnXNCEzg2DSdtjgtfXOetPNKfZAdeJ8-ULRFkDBeYQKtyuJxv9-',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)
content = content.split('(')[1].split(')')[0]
# print(content)
with open('074_urllib_jsonpath淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('074_urllib_jsonpath淘票票.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)
