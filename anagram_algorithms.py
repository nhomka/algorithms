import time
import random
def anagram_1(s1, s2):
    start = time.time()
    if len(s1) != len(s2):
        raise RuntimeError("Strings not of matching length")

    s2 = [i for i in s2]

    good = True
    for i in range(len(s1)):
        if not good:
            break
        run = False
        for j in range(i, len(s1)):
            if s1[i] == s2[j]:
                run = True
                s2[j], s2[i] = s2[i], s2[j]
                break
        good = run

    end = time.time()
    print(f"anagram_1 elapsed time = {end-start} seconds")
    return good

def anagram_2(s1, s2):
    start = time.time()
    if len(s1) != len(s2):
        raise RuntimeError("Strings not of matching length")
    
    a = [i for i in s1]
    b = [i for i in s2]

    a.sort()
    b.sort()
    
    end = time.time()
    print(f"anagram_2 elapsed time = {end-start} seconds")
    return a==b

def anagram_3(s1, s2): # dict
    start = time.time()
    if len(s1) != len(s2):
        raise RuntimeError("Strings not of matching length")

    d = {}
    for c in s1:
        d[c] = d.get(c, 0) + 1
    
    for c in s2:
        if c not in d or d[c] <= 0:
            end = time.time()
            print(f"anagram_3 elapsed time = {end-start} seconds")
            return False
        else:
            d[c] -= 1
            if d[c] == 0:
                del d[c]
    
    end = time.time()
    print(f"anagram_3 elapsed time = {end-start} seconds")
    return len(d) == 0

r1 = [chr(random.randrange(70, 90)) for _ in range(1000000)]
r2 = [i for i in r1]
random.shuffle(r2)
index = random.randint(0, len(r2)-1)
r2[index] = chr(ord(r2[index]) + 1)
a1, a2 = "fiesty little thing", "thest yifingel tilt" # True
b1, b2 = "fiesty little thing", "thest yifingel tils"# False
c1, c2 = "", ""# True
d1, d2 = "a", "a"# True
e1, e2 = "a", "b"# False
#print (anagram_1(r1, r2), anagram_2(r1, r2), anagram_3(r1, r2))
print (anagram_2(r1, r2), anagram_3(r1, r2))
            
