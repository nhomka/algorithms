import random

rand_list = list(range(1000))
random.shuffle(rand_list)
print(rand_list)

def merge(a, b):
    res = []
    
    a_ind = b_ind = 0

    while a_ind < len(a) or b_ind < len(b):
        if a_ind >= len(a):
            res.append(b[b_ind])
            b_ind += 1
        elif b_ind >= len(b):
            res.append(a[a_ind])
            a_ind += 1
        else:
            if a[a_ind] <= b[b_ind]:
                res.append(a[a_ind])
                a_ind += 1
            else:
                res.append(b[b_ind])
                b_ind += 1
    
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = (len(arr)//2)

    l = merge_sort(arr[0:mid])
    r = merge_sort(arr[mid:len(arr)])

    return merge(l, r)
#print(merge([1,3,5,7],[2,4,6,8])) 
resorted = merge_sort(rand_list) 
# test = [1,3,5,7,2,4,6,8]
# mid_test = len(test)//2
# print(test[0:mid_test], test[mid_test:-1])
print(resorted, resorted == list(range(1000)))

