from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    """Push
    add a new item to the END of the stack
    """

    def push(self, value):
        self.storage.add_to_tail(value)

    """Pop
    remove the last item in the stack
    """

    def pop(self):
        if not self.storage.tail:
            return
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
