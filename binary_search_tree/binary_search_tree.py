# from dll_stack import Stack
# from dll_queue import Queue
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
    # def get_max(self):
    #     pass

    # # Call the function `cb` on the value of each node
    # # You may use a recursive or iterative approach
    # def for_each(self, cb):
    #     pass

    # # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
