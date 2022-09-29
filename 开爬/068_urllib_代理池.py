# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 13:35
# @Author : fx
# @File : 068_urllib_代理池
# @Project : pythonProject
import random
proxies_pool = [
    {'http': '202.109.157.65:9000'},
    {'http': '201.129.157.65:9000'},
]

proxies = random.choice(proxies_pool)
print(proxies)