import time
def min_n2(items):
    start = time.time()
    res = float('inf')
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] < res:
                res = items[i]
    end = time.time()
    print(f"elapsed time n^2: {end-start} seconds")
    return res

def min_n(items):
    start = time.time()
    res = float('inf')
    for i in range(len(items)):
        if items[i] < res:
            res = items[i]
    end = time.time()
    print(f"elapsed time n: {end-start} seconds")
    return res

a = min_n2([i for i in range(10000, -1, -1)])
b = min_n([i for i in range(1000000, -1, -1)])
print(a, b)