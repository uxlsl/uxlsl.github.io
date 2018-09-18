---
layout: post
title: google-chrome安装
category: 学习
keywords: 学习,2018
---


# archlinux下的google-chrome安装


```


git clone https://aur.archlinux.org/google-chrome.git
makepkg -s
pacman -U google-chrome-xxxxx-x86_64.pkg.tar.xz


```


## 注意

1. 如果报md5的错误就要makepkg -s 加多一个--skipchecksums的参数
