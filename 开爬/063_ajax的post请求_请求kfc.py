# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 6:59
# @Author : fx
# @File : 063_ajax的post请求_请求kfc
# @Project : pythonProject
import urllib.request
import urllib.parse


def creat_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10,
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=base_url,data=data,headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    context = response.read().decode('utf-8')
    return context


def down_load(page, context):
    fp = open('kfc/kfc第' + str(page) + '页.json', 'w', encoding='utf-8')
    fp.write(context)
    fp.close()


if __name__ == '__main__':
    start_page = int(input('请输入起始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        context = get_content(request)
        down_load(page,context)
