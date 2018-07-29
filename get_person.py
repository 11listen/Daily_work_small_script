#!/usr/bin/env python
#coding:utf-8

import urllib.request
import re

def gethtml():
    reques = urllib.request.urlopen("http://xxx.xxx.xxx.xxx/xxpt/?q=node/people/get/70950")
    html = reques.read().decode('utf-8')
    return html


def pat():
    wangye = gethtml()
    pattern = r'.*?alt="(.*?)的头像.*?">(.*?)</div>.*?'
    parten = re.compile(pattern)

    all = parten.findall(wangye)
    with open("E://xxx.txt", "w+", encoding="UTF-8") as f:
        for phone, name in all:
            ss = '姓名：' +  name + '=======' + '电话：' + phone
            f.writelines(ss+"\t\n")
        f.close()
    print('done')

if __name__ == '__main__':
    pat()