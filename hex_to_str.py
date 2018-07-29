#coding: utf-8

#16进制转字符串

import binascii

def charac():
    chara = input("请输入要转换的十六进制字符串:")
    string = binascii.a2b_hex(chara)
    print(string)

charac()