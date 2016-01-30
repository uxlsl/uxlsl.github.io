---
layout: post
title: python-douban.fm-代码分析
category: 学习
keywords: 学习,2016
---



目录结构

doubanfm/
├── API
│   ├── api.py
│   ├── __init__.py
│   ├── json_utils.py
│   ├── login.py
│   ├── netease_api.py
│   └── __pycache__
├── check.py
├── colorset
│   ├── colors.py
│   ├── __init__.py
│   └── theme.py
├── config.py
├── controller
│   ├── help_controller.py
│   ├── __init__.py
│   ├── lrc_controller.py
│   ├── main_controller.py
│   ├── manager_controller.py
│   └── quit_controller.py
├── dal
│   ├── dal_help.py
│   ├── dal_lrc.py
│   ├── dal_main.py
│   ├── dal_manager.py
│   ├── dal_quit.py
│   └── __init__.py
├── data.py
├── douban.py
├── exceptions.py
├── getch.py
├── __init__.py
├── lrc2dic.py
├── model.py
├── notification.py
├── player.py
├── __pycache__
└── views
    ├── base_view.py
    ├── help_view.py
    ├── history_view.py
    ├── __init__.py
    ├── lrc_view.py
    ├── main_view.py
    ├── manager_view.py
    └── quit_view.py


## API目录
主要包括
login.py
api.py


### login.py分析

主函数:

request_token
win_login
get_captcha_id
get_captcha_pic

#### 关系

win_login 调用 get_captcha_id

captcha_id = get_captcha_id()

get_captcha_id(captcha_id)

request_token 返回一个token



#### 例子

demo/code/2016-1-30/douban.fm/test_login.py

```

# -*- coding: utf-8 -*-

from doubanfm.API import login


ret = login.request_token()

print(ret)


# --结果--
$ python test_login.py

➔ Email: Pythonista
➔ Password:
➔ Solution: screw
{'liked': 0, 'channel': 0, 'valume': 50, 'played': 0, 'theme_id': 0, 'banned': 0, 'user_name': 'Pythonista', 'cookies': <<class 'requests.cookies.RequestsCookieJar'>[Cookie(version=0, name='bid', value='"FfSvkDDv1kM"', port=None, port_specified=False, domain='.douban.fm', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1485675606, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False), Cookie(version=0, name='dbcl2', value='"141306659:7yoA/EaupdQ"', port=None, port_specified=False, domain='.douban.fm', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=None, discard=True, comment=None, comment_url=None, rest={'httponly': None}, rfc2109=False), Cookie(version=0, name='fmNlogin', value='"y"', port=None, port_specified=False, domain='.douban.fm', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1456731606, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)]>, 'is_pro': False}


```


### api.py代码分析

主要包含了Doubanfm 类,这个类的主要作用是与douban.fm服务交互.
Doubanfm 主要功能是
1. 播放音乐
2. 切换频道
3. 标记喜欢/取消喜欢

Doubanfm 查询播放列表(有点慢)


```

# -*- coding: utf-8 -*-


import time
import random
import json
import pprint
from doubanfm.API import api

douban = api.Doubanfm()
douban.set_channel(4)  # 粤语

ret = []
song = douban.get_first_song()
ret.append(song)
last = song
sid_set = set()
total = 0
try:
    while True:
        song = douban.get_song(last['sid'])
        if song['sid'] not in sid_set:
            sid_set.add(song['sid'])
            ret.append(song)
            print(song['title'])
            total += 1
            print('total {}'.format(total))
        time.sleep(random.randint(1, 5))

except (Exception, KeyboardInterrupt) as e:
    print(e)


json.dump(ret, open('playlist.json', 'w'))


```
