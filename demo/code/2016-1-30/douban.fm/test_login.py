# -*- coding: utf-8 -*-

from doubanfm.API import login


ret = login.request_token()

print(ret)
