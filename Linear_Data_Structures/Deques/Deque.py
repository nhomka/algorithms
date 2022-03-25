class Deque:
    """Create a Deque data structure from list"""

    def __init__(self) -> None:
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return self._items

    def add_front(self, item):
        self._items.insert(0, item)

    def add_back(self, item):
        self._items.append(item)
    
    def remove_front(self):
        return self._items.pop(0)

    def remove_back(self):
        return self._items.pop()