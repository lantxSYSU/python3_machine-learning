#如何实现用户的历史记录功能(最多n条)


#一个猜数字的游戏

from random import randint
from collections import deque
import pickle
import os

N = randint(0,100)
history = deque([], 5)
file = 'history'
if os.path.exists(file):
    history = pickle.load(open(file, 'wb+'))


def guess(k):
    if(k == N):
        print("right!")
        return True
    if(k < N):
        print("%s less than N" %k)
    else:
        print("%s greater than N" % k)
    return False

while True:
    line = input("please input a number:")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(history)


    pickle.dump(history, open(file, 'wb+'))
