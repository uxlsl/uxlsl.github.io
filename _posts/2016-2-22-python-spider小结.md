---
layout: post
title: python 爬虫小结
category: 学习
keywords: 学习,2016
---


## 关于网关

推荐使用
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
曾结使用其他时,服务器会判断出是机器人来的,使用这个就判断不出来!~~~


## 关于bs4
find系列无法对多层关系使用确定, 在此时使用select就可以解决这个问题,但 select 没有 select_all, 返回总是列表.

要*注意*的是 class_要加多一划线,

使用 bs4的例子!


```
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from jinja2 import Template


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
cookies = {}
jandan_url = 'http://jandan.net'
output = 'jandan.md'
TEMPLATE = """
# 煎蛋首页
{% for art in articles %}
![]({{ art.img_url }})
**文章标题**：{{ art.title }}
**文章链接**：[{{ art.href}}]({{ art.href }})
**标签**：{{ art.label }}
{% endfor %}
"""


def main():
    r = requests.get(jandan_url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(r.text, 'lxml')
    articles = []
    for i in soup.find_all(class_='post f list-post'):
        try:
            art = {}
            img = i.select('.thumbs_b a img')[0]
            if img.has_attr('src'):
                img_url = img['src']
            elif img.has_attr('data-original'):
                img_url = img['data-original']
            else:
                img_url = ''
            indexs_times = i.select('.indexs .time_s a')
            label = '/'.join([j.text for j in indexs_times])
            art['img_url'] = 'http:' + img_url
            art['label'] = label
            art['title'] = i.select('.indexs h2 a')[0].text
            art['href'] = i.select('.indexs h2 a')[0]['href']
            articles.append(art)
        except IndexError:
            pass

    template = Template(TEMPLATE)
    open(output, 'w').write(template.render(articles=articles))

if __name__ == '__main__':
    main()

```
