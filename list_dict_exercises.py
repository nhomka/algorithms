import random
import time
import timeit

l = list(range(10000))
la = list(range(10000000))

def l1():
    res = 0
    for i in range(1000000):
        res += l[random.randrange(0, len(l)-1)]
    print(res)

def l2():
    res = 0
    for i in range(1000000):
        res += la[random.randrange(0, len(la)-1)]
    print(res)

timer1 = timeit.Timer("l1", "from __main__ import l1")
print(f"l1 elapsed: {timer1.timeit(number=1000)} ms")
timer2 = timeit.Timer("l2", "from __main__ import l2")
print(f"l2 elapsed: {timer1.timeit(number=1000)} ms")