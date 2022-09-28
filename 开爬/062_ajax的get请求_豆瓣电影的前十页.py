# _*_ coding:utf-8 _*_
# @Time : 2022/9/28 23:17
# @Author : fx
# @File : 062_ajax
# @Project : pythonProject
import urllib.parse
import urllib.request


# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100:90&action=&
# start=40&limit=20
# https://movie.douban.com/j/chart/top_list?type=6&interval_id=100:90&action=&
# start=20&limit=20

def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100:90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)

    url = base_url + data
    # print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/104.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    context = response.read().decode('utf-8')
    return context


def down_load(page, context):
    fp = open('douban/豆瓣第' + str(page) + '页.json', 'w', encoding='utf-8')
    fp.write(context)
    fp.close()


if __name__ == '__main__':
    start_page = int(input('输入起始的页码数：'))
    end_page = int(input('输入结束的页码数：'))
    for page in range(start_page, end_page + 1):
        request = creat_request(page)
        context = get_content(request)
        down_load(page, context)
