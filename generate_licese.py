#coding: utf-8

#随机车牌生成

import random
import string

l = ["".join(random.sample(string.ascii_uppercase + string.digits, 5)) for i in range(100)]
print(l)
