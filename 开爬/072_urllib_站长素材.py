# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 16:08
# @Author : fx
# @File : 072_urllib_站长素材
# @Project : pythonProject
import urllib.request
from lxml import etree


# https://sc.chinaz.com/tupian/rentiyishu.html
# https://sc.chinaz.com/tupian/rentiyishu_2.html
# https://sc.chinaz.com/tupian/rentiyishu_3.html


def creat_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/rentiyishu.html'
    else:
        url = 'https://sc.chinaz.com/tupian/rentiyishu_' + str(page) + '.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36'
    }
    # print(url)
    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="bot-div"]/a/@title')
    # src_list = tree.xpath('//div[@class="item masonry-brick"]/img/@src')
    # 为啥改成item就可以
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        url = url.replace('_s', '')
        urllib.request.urlretrieve(url=url, filename='./站长素材/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始代码：'))
    end_page = int(input('请输入结束代码：'))
    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        content = get_content(request)
        down_load(content)
