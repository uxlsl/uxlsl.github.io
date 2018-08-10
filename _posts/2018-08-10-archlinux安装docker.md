
---
layout: post
title:
category: 学习
keywords: 学习,2018
---


# archlinux 安装docker
安装

1. 

```

pacman -S docker



```

2. 启动docker

如果发现报错

```


journalctl -u docker


```

如果发现这个问题

1. There are no more loopback devices available.

重启机子

2.  docker pull 出现没有权限则

```

sudo usermod -a -G docker lin


```
