---
layout: post
title: flask-login的一些笔记
category: 学习
keywords: 学习,2016
---

## flask-login的安装

pip install flask-login


## 关健配置

```

app.secret_key = '*****'

## 配置一些属性！

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

＠login_manager.user_loader
def user_loader(user_id):
# 返回 flask_login.UserMixin or None

# user UserMixin类型
flask_login.login_user(user)


```

## 工作流

@login_reqire -> login_manager -> login界面 -> login_user -> ... -> logout_user
