# Stack
# Only the top node is accessible
# both read and write

# Adding an item to the stack O(1)

# Retrieving an item form the stack also
class InvalidOperationError(BaseException):
    pass
class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack():
    # FILO
    def __init__(self, node = None):
        self.top = node
    
    def push(self, value):
        # create node from value
        node = Node(value)
        # point new node to top
        node.next = self.top
        # assign node to top
        self.top = node
    
    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        # create temp node
        # assign top to the temp node
        node = self.top
        # top reassign it to top.next
        self.top = self.top.next
        # return value of temp node
        return node.value
    
    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value
    
    def is_empty(self):
        return True
    

class Queue():
        # FIFO
    def __init__(self):
        self.front = None
        self.rear = None