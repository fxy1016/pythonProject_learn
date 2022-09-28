# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 8:04
# @Author : fx
# @File : 057_urllib_get请求的quote方法
# @Project : pythonProject
import urllib.request
import urllib.parse
# https://www.baidu.com/s?ie=UTF-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
url = 'https://www.baidu.com/s?ie=UTF-8&wd='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
name = urllib.parse.quote('周杰伦')
url = url + name
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
context = response.read().decode('utf8')
print(context)

