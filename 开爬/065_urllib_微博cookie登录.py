# _*_ coding:utf-8 _*_
# @Time : 2022/9/29 9:19
# @Author : fx
# @File : 065_urllib_微博cookie登录
# @Project : pythonProject
import urllib.request

url = 'https://weibo.com/u/2016713117'
headers = {
    'set-cookie': 'WBPSESS=VC13eXCDS6sgLONS22hQp6Z7jKqHQFxQuITf3kET94KuIbLd95bMaUhKR-MlG'
                  '-ruwsDqtgft8DDtrNiYB6idUsD3Q9WgfjBNeePEMFd_w6jGq_SUV2AZLTHGP8OB3nlU9zV6OzA6Jtzwzo-q5iSUVQ==; '
                  'path=/; max-age=86400; expires=Fri, 30 Sep 2022 01:29:47 GMT; secure; httponly',
    'cookie': 'SINAGLOBAL=2140922359202.4773.1661838540204; XSRF-TOKEN=YlSEk_IDlDFK7x2alUinfOTQ; PC_TOKEN=82db365b09; '
              'login_sid_t=d8ff23ff39c771cd4b4b1e388bc31ca7; cross_origin_proto=SSL; _s_tentry=weibo.com; '
              'Apache=1918606396217.0374.1664414273615; '
              'ULV=1664414273620:2:1:1:1918606396217.0374.1664414273615:1661838540246; '
              'SUB=_2A25OMII_DeRhGeFJ7VcW9i_KzTqIHXVtR_T3rDV8PUNbmtAKLRHYkW9Nf0taBmCD5hng9D0258S9pjLdZdz5a7cJ; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WheXyrAy_vEPq07ivdn_4jU5JpX5KzhUgL.FoMNSo-NSo2cSoq2dJLoIc7LxK'
              '.LBKeL1KnLxKqL1-BLBK-LxK.LBKeL1KnLxK-L12-LB.zLxKML1-2L1hBLxKBLB.2L1K2LxKqL1-eL1h.LxKBLBonL1h5LxKML1h'
              '.L1hMLxK-L1-eLBKnLxK-LBKBLBK.LxKMLBK.LB.2t; ALF=1695950319; SSOLoginState=1664414319; wvr=6; '
              'webim_unReadCount=%7B%22time%22%3A1664414328478%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0'
              '%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D; '
              'WBPSESS=VC13eXCDS6sgLONS22hQp6Z7jKqHQFxQuITf3kET94KuIbLd95bMaUhKR-MlG'
              '-rujy0V5jUZvI9hcm0ByD4Hxf3IbmNiArbPYjHsIXAMvxY3SYLYGE9D-ZLedLn0vhvm5R9auRZ3SGHowRangaU0ZA==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
# 反扒手段，错误编码
content = response.read().decode('utf-8')
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
