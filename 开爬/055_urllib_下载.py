# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 7:33
# @Author : fx
# @File : 055_urllib_下载
# @Project : pythonProject

import urllib.request
# # 下载网页
# url_page = 'http://www.baidu.com'
# urllib.request.urlretrieve(url_page,'baidu.html')

# # 下载图片
# url_pic = 'https://bkimg.cdn.bcebos.com/pic/5ab5c9ea15ce36d3f4589cd334f33a87e850b1f0?x-bce-process=image/resize,m_lfit,w_536,limit_1/format,f_jpg'
# urllib.request.urlretrieve(url_pic,'fuhuanghou.jpg')

# 下载视频
url_video = 'https://baike.baidu.com/00d67ac9-6616-431e-ad7a-2df04a5a6c02'
urllib.request.urlretrieve(url_video,'jiaran.mp4')









































