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
