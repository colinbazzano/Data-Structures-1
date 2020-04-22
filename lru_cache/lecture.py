from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, limit=10):
        self.storage = {}
        self.ordering = DoublyLinkedList()
        self.size = 0  # keep track of how many items we have in our cache

    def __len__(self):
        return self.size

    def get(self, key):
        # check to see that the key is in our cache
        if key in self.storage:
            # fetch the DLL node which is the value of this key
            node = self.storage[key]
            self.ordering.move_to_end(node)
            # second item in the tuple aka the VALUE (key, value)
            return node.value[1]
        else:
            return None  # we don't have that key in our cache

    def set(self, key, value):
        # check if the key is in the cache
        if key in self.storage:
            node = self.storage[key]  # fetch the node
            # overwrite the old value
            node.value = (key, value)
            # move this node to the tail (most recently used)
            self.ordering.move_to_end(node)
            return
        if self.size == self.limit:
            # first evict the LRU element
            oldest_key = self.ordering.head.value[0]
            del self.storage[oldest_key]
            # remove the head node from the DLL
            self.ordering.remove_from_head()
            self.size -= 1
        # key is not in self.storage and we still have room in our cache
        # add the key and value
        self.ordering.add_to_tail((key, value))
        self.storage[key] = self.ordering.tail
        self.size += 1
