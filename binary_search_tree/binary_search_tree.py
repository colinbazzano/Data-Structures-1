# from dll_stack import Stack
# from dll_queue import Queue
from collections import deque
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # check if self.left is a valid node
            if self.left:  # is Not None / is there a node here
                self.left.insert(value)
            # base case - the left side is empty
            else:
                # we've found our valid parking spot
                self.left = BinarySearchTree(value)
        # otherwise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value is the target, we're done!
        if self.value == target:
            return True
        if target >= self.value and self.right:  # if the target is greater than or equal to AND self.right is valid
            # call the function again recursively on the right (greater than) side
            return self.right.contains(target)
        elif target < self.value and self.left:
            # call the function again recursively on the left (less than) side
            return self.left.contains(target)
        else:
            return False  # not here

    # Return the maximum value found in the tree
    def get_max(self):
        # we will only work with the right side, as the left side can never be the max num
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.right and self.left:
            cb(self.value)
            self.right.for_each(cb)  # call it again on the items to the right
            self.left.for_each(cb)  # call it again on the items to the left
        elif self.left:  # no more to the right, but still more to left
            cb(self.value)
            self.left.for_each(cb)
        elif self.right:  # no more to the left, but still more to the right
            cb(self.value)
            self.right.for_each(cb)
        else:
            cb(self.value)

    # LECTURE SOLUTION TO FOR EACH
    # at least O(n), could be worse depending on the callback
    def for_each2(self, cb):
        # apply the callback
        cb(self.value)
        # base case: the node has no children
        # call the cb on the children of this noe
        # check that the node has children
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def depth_for_each(self, cb):
        stack = []

        # add the root of the tree to the stack
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current_node = stack.pop()
            # check if the right child exists
            if current_node.right:
                stack.append(current_node.right)
            # check if the left child exists
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_for_each(self, cb):
        # depth first : stack
        # breadth-first : queue
        q = deque()  # create your queue
        q.append(self)  # append the root

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:  # if we have nodes to the left...
                q.append(current_node.left)  # ...append it!
            if current_node.right:  # if we have nodes to the right...
                q.append(current_node.right)  # ...append it!
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if not node:
            return
        self.in_order_print(node.left)
        self.in_order_print(node.right)
        # if self.left:
        #     self.left.in_order_print(self.value)
        # if self.right:
        #     self.right.in_order_print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
