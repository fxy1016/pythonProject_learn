# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 13:17
# @Author : fx
# @File : 086_requests_post
# @Project : pythonProject
import requests
import json

url = 'https://fanyi.baidu.com/sug'

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '10',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=C03D58E94AAE8EB66CAC85F152C966F5; PSTM=1653319103; BAIDUID=C03D58E94AAE8EB6C74D07001522D8ED:SL=0:NR=10:FG=1; BDUSS=x1NHRafkItWEl3alNvMy1XN09jSn5RMWhiYnByaDVKNm42akZ4RzM5UzRmMXRqRVFBQUFBJCQAAAAAAQAAAAEAAADdV0cksNm2vs~ey9nLvsLtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALjyM2O48jNjZU; BDUSS_BFESS=x1NHRafkItWEl3alNvMy1XN09jSn5RMWhiYnByaDVKNm42akZ4RzM5UzRmMXRqRVFBQUFBJCQAAAAAAQAAAAEAAADdV0cksNm2vs~ey9nLvsLtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALjyM2O48jNjZU; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=37147_36550_37299_36885_37402_37396_36804_37404_36786_37500_26350_37478_37370; delPer=0; PSINO=7; BA_HECTOR=8024a1ah2581012g242h7la81hjfj081b; ZFY=x:BU1j621lMyTwn13YB5wrp:AV8VMpPiPWqQZr0ztkvfA:C; BAIDUID_BFESS=C03D58E94AAE8EB6C74D07001522D8ED:SL=0:NR=10:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1664367018,1664367923,1664601426; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1664601433',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'kw': 'pass'
}

response = requests.post(url=url, headers=headers, data=data)
# response.encoding='utf-8'
content = response.content
# print(content)
obj = json.loads(content)
print(obj)
