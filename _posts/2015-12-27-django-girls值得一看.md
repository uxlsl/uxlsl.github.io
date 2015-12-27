---
layout: post
title: django girls 值得一看
category: 学习
keywords: 学习,2015
---

![internet_4.png](http://tutorial.djangogirls.org/zh/how_the_internet_works/images/internet_4.png)

![internet](http://tutorial.djangogirls.org/zh/how_the_internet_works/images/internet_2.png)


> We inspire women to fall in love with programming.

> Django Girls organize free Python and Django workshops, create open sourced online tutorials and curate amazing first experiences with technology.

# 原因

1. 简单
2. 容易表达
3. 面向群体是women
总结: 看看别人是怎样表达一件事,如何沟通.


# 摘抄了一些句子(我看的是中文版)

> Django （/ˈdʒæŋɡoʊ/jang-goh） 是用 Python 写的一个自由和开放源码 web 应用程序框架。 web框架是一套组件，能帮助你更快、更容易地开发web站点。

> 当你开始构建一个web站点时，你总需要一些相似的组件：处理用户认证（注册、登录、登出）的方式、一个管理站点的面板、表单、上传文件的方式，等等。

> 幸运的是，其他人很早就注意到web开发人员会面临一些共同的问题。所以他们联手创建了 web 框架（Django 是其中一个）来让你使用。

> 由于框架的存在，你无需重新发明轮子就能建立新的站点。


>  Django 需要固定的系统结构，以便 Django 能够找到重要的东西。

> 想象一个邮递员拿着一封信。 她沿着街区走下去，检查每一个房号与信件地址是否对应。 如果匹配上了，她就把信投在那里。 这也是url解析器的工作方式！

> 现在你可以来杯咖啡(或者是茶) 或吃点东西给自己充下电，你刚刚创建了你的第一个Django模型，这是你应得的。

> 我们将使用 GitHub 作为基石，以和 PythonAnywhere 互相传输我们的代码。

> "It works" 不见了，啊？不要担心，这只是个错误页面，不要被吓到了。它们实际上是非常有用的：

> manage.py 是一个帮助管理站点的脚本。

> 还有一件事：部署时刻！



# 一些代码


```

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


```

# 参考
[djangogirls入门教程中文版](http://tutorial.djangogirls.org/zh/django/index.html)
