---
layout: post
title: django-timezone 时区笔记
category: 学习
keywords: 学习,2016
---

# 定义

> When support for time zones is enabled, Django stores datetime information in UTC in the database, uses time-zone-aware datetime objects internally, and translates them to the end user’s time zone in templates and forms.

> 当打开时区开关时,django存储时间到数据库使用utc格式,直接使用国际化的对象,通过模板和表格将时间转换合适的形式给终端用户.


# 为什么使用utc格式存储时间

> Even if your website is available in only one time zone, it’s still good practice to store data in UTC in your database. The main reason is Daylight Saving Time (DST). Many countries have a system of DST, where clocks are moved forward in spring and backward in autumn. If you’re working in local time, you’re likely to encounter errors twice a year, when the transitions happen. (The pytz documentation discusses these issues in greater detail.) This probably doesn’t matter for your blog, but it’s a problem if you over-bill or under-bill your customers by one hour, twice a year, every year. The solution to this problem is to use UTC in the code and use local time only when interacting with end users.

**强烈要求安装pytz*

```

pip install pytz

```

# Naive and aware datetime objects(普通时间和时区时间)


```

import datetime

now1 = datetime.datetime.now() # naive

from django.utils import timezone

now2 = timezone.now() # aware 国际性的时间,能在全球性转换

timezone.is_naive(now1)
timezone.is_aware(now2) #是不是国际时间


```

# Interpretation of naive datetime objects (与通用时间交互)

思考当配置 USE_TZ=True时,一个普通时间存储在数据库时会发生什么情况?

When USE_TZ is True, Django still accepts naive datetime objects, in order to preserve backwards-compatibility. When the database layer receives one, it attempts to make it aware by interpreting it in the default time zone and raises a warning.

简单地存储和警告!


# Default time zone and current time zone (设定时区)

The default time zone is the time zone defined by the TIME_ZONE setting.

The current time zone is the time zone that’s used for rendering.

You should set the current time zone to the end user’s actual time zone with activate(). Otherwise, the default time zone is used.

简洁,设置时区.


```


import pytz

from django.utils import timezone

class TimezoneMiddleware(object):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()


```

# 模块时间的一些应用

总体来说就是打开与关闭


# 例子

./demo/code/2016-1-20/mytimezone 显示所有时区的时间


# 额外
*如果想要在代码中使用本地时间有如下方法*:
1.
now.astimezone(pytz.timezone(settings.TIME_ZONE))))

# 参考

django-1.9/topics/i18n/timezones.html
django-1.9/ref/templates/builtins.html#date
