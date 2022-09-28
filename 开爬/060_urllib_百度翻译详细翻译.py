# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 20:38
# @Author : fx
# @File : 060_urllib_百度翻译详细翻译
# @Project : pythonProject

import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
    'Acs-Token': '1664348654757_1664368663703_GnQOAwWD5Wzef65kuabqWlSIopRJCh4KnHXkBtpOt7xCib3lojSbcbmdh1p+8b791PdFOrrJhyk6AW11fQaYKW8Mb1pJvXdG7ryGTeMfStG1iQ2F7uk9bj5Koj3IzZUwP65dKeJlgSqdR1z//7oN38RJF7oqw/DNPCMzCB8NUfMGpFnKAI85YwEDOj992b93GetyqRseJ9zqn6toPlvNUCj5m1t9EPBBeyWUBVARPBAa+TSUpV/rXqL6fgNrgKqEA3v7nn7EjOmXcYLfoi7PFL67XqWHoW0DGEEihh+gF5TJYW5YlSOfNSYNUU3m34u32dXs6GZRZCKzqEkQ2FjA/g==',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=C03D58E94AAE8EB66CAC85F152C966F5; PSTM=1653319103; BAIDUID=C03D58E94AAE8EB6C74D07001522D8ED:SL=0:NR=10:FG=1; BDUSS=x1NHRafkItWEl3alNvMy1XN09jSn5RMWhiYnByaDVKNm42akZ4RzM5UzRmMXRqRVFBQUFBJCQAAAAAAQAAAAEAAADdV0cksNm2vs~ey9nLvsLtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALjyM2O48jNjZU; BDUSS_BFESS=x1NHRafkItWEl3alNvMy1XN09jSn5RMWhiYnByaDVKNm42akZ4RzM5UzRmMXRqRVFBQUFBJCQAAAAAAQAAAAEAAADdV0cksNm2vs~ey9nLvsLtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALjyM2O48jNjZU; BAIDUID_BFESS=C03D58E94AAE8EB6C74D07001522D8ED:SL=0:NR=10:FG=1; RT="z=1&dm=baidu.com&si=abwgz2vldb&ss=l8lkmn2c&sl=4&tt=9vb&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=bju&ul=geo&hd=gta"; BA_HECTOR=8ga42485aha0a10h84204mkq1hj8dim1b; ZFY=eHP6apwJaA:BkplAc:A3qwuEPyTlFM4KK45:B1Df:BTXfzU:C; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=37147_36550_37299_36885_37396_36804_37404_36786_37500_26350_37478_37370; delPer=0; PSINO=6; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664367018,1664367923; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664367923',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '34a6723c01f9678259c8bff73b3d0fe0',
    'domain': 'common'
}

data = urllib.parse.urlencode(data).encode('utf-8')


request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
context = response.read().decode('utf-8')
# print(context)

obj = json.loads(context)
print(obj)