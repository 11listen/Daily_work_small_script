#/usr/bin/env python
#coding: utf-8

import codecs
import re

#读取网站主机文件
def ls():
    with open("E://host.dat") as hosts:
        return [host.strip("\n") for host in hosts.readlines()]


#读取IDS规则文件
def di():
    with codecs.open("E://urls.rules", encoding="utf-8") as rules:
        return [rule.strip("\r\n") for rule in rules.readlines()]


#主机文件替换规则中的某些部分
def sudo():
    zhuji = ls()
    guize = di()
    num = 8001000
    import re
    res = []


    for i in range(len(ls())):
        rep = zhuji[i]
        line = guize[i]
        partern = """.*?content:"(.*?)";reference: url, (.*?); tag: session,3000,packets; sid: (.*?);.*?"""
        gaim = re.findall(partern, line)[0]
        num += 1
        new = str(num)
        if num < 10:
            new = "0"+str(num+1)

        g_res = line.replace(gaim[0], str(rep[4:])).replace(gaim[1], str(rep)).replace(gaim[2], new, 1)
        print(g_res)
        res.append(g_res)
    # print(res)
    with codecs.open("E://unew_rls.rules", "w+", encoding="utf-8") as f2:
        [f2.write(x+"\n") for x in res]
        f2.close()

if __name__ == "__main__":
    sudo()