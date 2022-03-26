from Queue import Queue
from random import randrange

def hot_potato(name_list, rand_max):
    potato_queue = Queue()

    for i in name_list:
        potato_queue.enqueue(i)

    while potato_queue.size() > 1:
        for i in range(randrange(1, rand_max + 1)):
            potato_queue.enqueue(potato_queue.dequeue())
        potato_queue.dequeue()

    return potato_queue.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))