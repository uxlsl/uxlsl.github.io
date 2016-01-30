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


## player.py 代码分析

主要有二个类
继承关系

Player
|
Mplayer

### 原理
运行播放器,并且使用看门狗监控播放器的运行状态.

不明白的
queue应该从中get, 但使用get_playingsong和get_song

例子

```

queue = XXX

mplayer = MPlayer()
mplayer.start_queue()
# 之后就会启动一个看门狗线程,监控mplayer
# 一旦终止,就会从队列从取出新的播放曲目给mplayer启动.

```

### 例子一个只播放指定电台的脚本

./demo/code/2016-1-30/douban.fm/playonefm.py

```

# -*- coding: utf-8 -*-
import time
from doubanfm import player
from doubanfm.API import api


class PlayerQueue:

    def __init__(self, douban):
        self.douban = douban
        self.current_song = douban.get_first_song()

    def get_playingsong(self):
        return self.current_song

    def get_song(self):
        self.current_song = self.douban.get_song(self.current_song['sid'])
        print(self.current_song['title'])
        return self.current_song


def main():
    import sys
    # 4 是粤语
    channel = int(sys.argv[1])
    douban = api.Doubanfm()
    douban.set_channel(channel)
    queue = PlayerQueue(douban)
    mplayer = player.MPlayer()
    mplayer.start_queue(queue)

    while True:
        if not mplayer.is_alive:
            break
        time.sleep(5)

if __name__ == '__main__':
    main()


```


## doubanfm/model.py 代码分析

主要有三个类.
Playlist,History,Channel

Playlist类主要封装了Doubanfm类,并在其基础上作了一些扩展,
比如在提前把播放列表拿下来(_watchdog).

例子:
使用 Playlist类对前面的例子作了改进,但不知如何打印当前歌曲!

./demo/code/2016-1-30/douban.fm/playonefm.py

```

# -*- coding: utf-8 -*-
import time
from doubanfm import player
from doubanfm.model import Playlist


def main():
    import sys
    # 4 是粤语
    channel = int(sys.argv[1])
    playlist = Playlist()
    playlist.set_channel(channel)
    mplayer = player.MPlayer()
    mplayer.start_queue(playlist)

    while True:
        if not mplayer.is_alive:
            break
        time.sleep(5)

if __name__ == '__main__':
    main()


```


## check.py 代码分析

主要包含
is_latest
update_package
is_mplayer

学习点:
pip包的使用


```

import pip

pip.main(['install', package_name, '--upgrade'])

# 检查 mplayer,是不是存在这个程序!

subprocess.check_output


```


## getch.py 代码分析

好像作者是为了让输入不显示,所以用这个文件的
看文件头

"""
Copyright (c) 2006-2015 sqlmap developers (http://sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

可以看出作者门也看了不少代码.


简单说明如何使用这个包,之于代码为什么这个实现,我先不进行研究.

```

In [1]: from doubanfm.getch import getch

In [2]: getch()
Out[2]: 'h'


```


## douban.py 代码分析

主要看看门狗程序的切换页面



```

class Router(object):
    """
    集中管理view之间的切换
    """

    def __init__(self):
        self.player = MPlayer()
        self.data = data.Data()
        self.quit_quit = False

        self.switch_queue = Queue.Queue(0)

        self.view_control_map = {
            'main': MainController(self.player, self.data),
            'lrc': LrcController(self.player, self.data),
            'help': HelpController(self.player, self.data),
            'manager': ManagerController(self.player, self.data),
            'quit': QuitController(self.player, self.data)
        }

        # 切换线程
        Thread(target=self._watchdog_switch).start()

    def _watchdog_switch(self):
        """
        切换页面线程
        """
        # init
        self.view_control_map['main'].run(self.switch_queue)

        while not self.quit_quit:
            key = self.switch_queue.get()
            if key == 'quit_quit':
                self.quit_quit = True
            else:
                self.view_control_map[key].run(self.switch_queue)

        # 退出保存信息
        self.quit()
        os._exit(0)

    def quit(self):
        # 退出保存信息
        self.data.save()
        subprocess.call('echo -e "\033[?25h";clear', shell=True)


```
