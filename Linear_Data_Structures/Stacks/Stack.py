class Stack:

    def __init__(self):
        self._items = []

    def push(self, val):
        self._items.append(val)

    def pop(self):
        return None if not self._items else self._items.pop()

    def peek(self):
        return None if not self._items else self._items[-1]

    def is_empty(self):
        return not self._items

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return f"Stack({self._items})"

def rev_string(my_str):
    stack = Stack()
    for c in my_str:
        stack.push(c)
    res = []
    while not stack.is_empty():
        res.append(stack.pop())
    return ''.join(res)
    

# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push('dog')
# print(s.peek())
# s.push(True)
# print(s.size())
# print(s.is_empty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.size())
# print (rev_string("hello"))
# print(rev_string("apple") == "elppa")
# print(rev_string("x") == "x")
# print(rev_string("1234567890") == "0987654321")