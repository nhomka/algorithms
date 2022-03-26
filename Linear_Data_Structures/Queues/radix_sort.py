from Queue import Queue

def radix_sort(int_list):
    bucket = Queue()
    res = []
    hi = max(int_list)

    for i in int_list:
        bucket.enqueue(f"{i:3d}")
    int_queues = {str(i): Queue() for i in range(10)}
    
    base = 1

    while base <= hi:
        for _ in range(bucket.size()):
            cur = bucket.dequeue()
            if base <= len(str(int(cur))):
                int_queues[cur[-base]].enqueue(cur)
            else:
                int_queues['0'].enqueue(cur)
        
        for q in int_queues.values():
            while not q.is_empty():
                bucket.enqueue(q.dequeue())

        base += 1
    return [int(bucket.dequeue()) for _ in range(bucket.size())]


print(radix_sort([101, 2, 11, 12]))