#/usr/bin/env python
#coding: utf-8

files = open("C:\\Users\\admin\\Desktop\\1.txt")

for line in files:
    with open("C:\\Users\\admin\\Desktop\\file.txt", "a") as f:
        print(f.writelines(line+'\n'))