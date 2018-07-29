#coding: utf-8

#局域网主机存活扫描

import shlex, subprocess

def scan(com):
    command = com
    args = shlex.split(command)
    exe = subprocess.Popen(args)
    return exe

com = input("请输入命令：")
crt = scan(com)
print(crt)

'''
command = "whoami"
args = shlex.split(command)
exe = subprocess.Popen(args)
print(exe)
'''