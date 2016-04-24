# -*- coding: utf-8 -*-
import itertools
import requests
import grequests
import BeautifulSoup as bs4
from datetime import datetime
import pprint

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'}
url = 'http://www.xicidaili.com/nn/{num}'
# ip_test_url = "http://ip.chinaz.com/getip.aspx"
ip_test_url = "http://httpbin.org/ip"


def get_ips(url, dt):
    ret = []
    for num in itertools.count(1):
        r = requests.get(url.format(num=num), headers=headers)
        soup = bs4.BeautifulSoup(r.text)
        table = soup.find('table', id='ip_list')
        if table:
            for item in table.findAll('tr', {'class': 'odd'}):
                tds = item.findAll('td')
                ip = tds[2].contents[0].strip()
                port = tds[3].contents[0].strip()
                ip_type = tds[6].contents[0].strip()
                ip_dt = datetime.strptime(
                    tds[-1].contents[0].strip(), '%y-%m-%d %H:%M')
                if dt.date() != ip_dt.date():
                    return ret
                ret.append({'ip': ip, 'port': port, 'type': ip_type})

        else:
            break
    return ret


def get_ips_can_connect(ips, ip_test_url=ip_test_url, count=2, hit=1):
    """获取能连接的ip代理
    params ips: list
    `ips item`:dict, ip, port
    params count: 测试次数
    params hit: 要通过次数
    """

    ret = []
    ip_counts = [0 for i in ips]

    for i in xrange(count):
        rs = []
        for item in ips:
            proxies = {item['type']: '{type}://{ip}:{port}'.format(type=item['type'],
                                                                   ip=item[
                                                                       'ip'],
                                                                   port=item['port'])}
            s = requests.Session()
            s.proxies = proxies
            rs.append(grequests.get(ip_test_url, session=s, timeout=10))
        ret = grequests.map(rs)
        for i, v in enumerate(ret):
            if v:
                ip_counts[i] += 1

    return [ip for i, ip in enumerate(ips) if ip_counts[i] >= hit]


if __name__ == '__main__':
    ips = get_ips(url, datetime.now())
    ips = get_ips_can_connect(ips)

    for i in ips:
        print('{0}://{1}:{2}'.format(i['type'].lower(), i['ip'], i['port']))
