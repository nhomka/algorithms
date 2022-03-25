from email import header
from os import remove
from Node import Node

class UnorderedList:

    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def search(self, search_val):
        cur = self.head
        while cur:
            if cur.value == search_val:
                return True
            cur = cur.next
        return False

    def remove(self, remove_val):
        prev = None
        cur = self.head
        while cur:
            if cur.value == remove_val:
                if not prev:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
        raise ValueError(f"Item with value: {remove_val} not found in Unordered List")

my_list = UnorderedList()

my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))

my_list.add(100)
print(my_list.search(100))
print(my_list.size())

my_list.remove(54)
print(my_list.size())
my_list.remove(93)
print(my_list.size())
my_list.remove(31)
print(my_list.size())
print(my_list.search(93))

try:
    my_list.remove(27)
except ValueError as ve:
    print(ve)