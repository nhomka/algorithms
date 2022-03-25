from Deque import Deque

def pal_checker(s) -> bool:
    dq = Deque()

    for char in s:
        dq.add_front(char)

    while dq.size() > 1:
        if dq.remove_back() != dq.remove_front():
            return False

    return True


print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))