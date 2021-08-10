#!/usr/bin/python3

import csv
from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])
def R_Csv():
    with open('/Users/1isten/Desktop/测试/________________________________________ko256z.csv', newline='') as c:
        s = csv.reader(c)
        for row in s:
            l = str(row)
            ch = translator.translate(l, src='en', dest='zh-cn')
            y = (str(ch))
            k = y.split(r'Translated(src=en, dest=zh-cn, text=')
            x = k[1]
            r = x
            return r


if __name__ == '__main__':
    R_Csv()
