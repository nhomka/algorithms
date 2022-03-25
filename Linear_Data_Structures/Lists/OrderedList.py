from Node import Node

class OrderedList:

    def __init__(self) -> None:
        self.head = None
        
    def size(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        return self.head == None

    def add(self, val):
        temp = Node(val)
        cur = self.head
        prev = None
        
        while cur and cur.value < val:
            prev = cur
            cur = cur.next

        if not prev:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = cur
            prev.next = temp

    def search(self, search_val):
        cur = self.head
        while cur and search_val >= cur.value:
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
            elif cur.value > remove_val:
                break
            prev = cur
            cur = cur.next
        raise ValueError(f"Item with value: {remove_val} not found in Unordered List")

my_list = OrderedList()
my_list.add(31)
my_list.add(77)
my_list.add(17)
my_list.add(93)
my_list.add(26)
my_list.add(54)

print(my_list.size())
print(my_list.search(93))
print(my_list.search(100))