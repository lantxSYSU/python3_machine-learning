#如何让字典保持有序
#使用collections 下ordereddict



from time import time
from random import randint
from collections import OrderedDict

players = list('abcdefgh')

start = time()
d = OrderedDict()

for i in range(8):
    input()
    p = players.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, p, end - start)
    d[p] = (i + 1, end - start)


print()
print('-'*20 )
for k in d:
    print(k, d[k])