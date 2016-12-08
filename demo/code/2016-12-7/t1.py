# -*- coding:utf-8 -*-

import json

with open('t1.json', 'w') as f:
    for i in range(0, 100):
        f.write('{}\n'.format(json.dumps((i,i*i))))
