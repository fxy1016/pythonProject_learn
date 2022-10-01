# _*_ coding:utf-8 _*_
# @Time : 2022/10/1 16:07
# @Author : fx
# @File : 088_requests_cookie_古诗词网
# @Project : pythonProject
import requests
from bs4 import BeautifulSoup
import urllib.request

url_login_page = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.0.0 Safari/537.36'
}
response = requests.get(url=url_login_page, headers=headers)
response.encoding = 'utf-8'
content = response.text

soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code = soup.select('#imgCode')[0].attrs.get('src')
real_code_src = 'https://so.gushiwen.cn' + code
# 会请求新的验证码，所以不能用
# urllib.request.urlretrieve(real_code_src, 'code_gushiwen.png')
# print(code)
# print(real_code_src)

# session
session = requests.session()
# 验证码url的内容
response_code = session.get(real_code_src)

content_code = response_code.content
with open('code.jpg','wb') as fp:
    fp.write(content_code)

code_name = input('输入验证码：')

data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'fxinsky@163.com',
    'pwd': 'gushiwenwaaa',
    'code': code_name,
    'denglu': '登录',
}

response_post = session.post(url=url_login_page, headers=headers, data=data_post)
content_post = response_post.text

with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
