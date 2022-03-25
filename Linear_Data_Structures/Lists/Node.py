class Node:
    """A node of a linked list"""

    def __init__(self, val) -> None:
        self._val = val
        self._next = None

    def get_val(self):
        return self._val

    def set_val(self, val):
        self._val = val

    value = property(get_val, set_val)

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node

    next = property(get_next, set_next)

    def __str__(self) -> str:
        return str(self._val)