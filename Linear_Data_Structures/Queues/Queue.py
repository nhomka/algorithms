class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not self._items

    def size(self):
        """Return the number of items in the queue"""
        return len(self._items)

    def enqueue(self, item):
        """Insert a new item into the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove the next item from the queue"""
        return self._items.pop()
