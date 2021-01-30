# Node based data structure

class Node:
    ''' We need to point to two other nodes ina a Binary Tree so the Node must have two pointers
        Traditionally they are called 'left' and 'right'
    '''
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        def traverse(root):
            # print root first
            print(root.value)
            # traverse left second
            if root.left:
                traverse(root.left)
            # traverse right last
            if root.right:
                traverse(root.right)
        traverse(self.root)

# root <= self.root <= A
# output A
# check LHS
    # root <= root.left <= B
    # output B
    # check LHS
        # root <= root.left <= D
        # output D
        # check LHS
        # check RHS
    # check RHS
        # root <= root.left <= E
        # output E
        # check LHS
        # check RHS
# check RHS
    # root <= root.left <= C
    # output C
    # check LHS
    # check RHS

    def pre_order2(self):
        def traverse(root):
            # if there is no node here then exit
            if not root: # base case
                return
            # print root first
            print(root.value)
            # traverse left
            traverse(root.left)
            # traverse right
            traverse(root.right)
        traverse(self.root)

    def pre_order3(self, current_root = None, is_root = False):
        # DO NOT DO THIS #
        # if there is no current node here assume we are at the root
        if is_root: # I feel sick inside
            current_root = self.root
        # if there is no current node here then exit
        if not current_root: # base case
            return
        # operate on root first
        print(current_root.value)
        # traverse left second
        self.pre_order3(current_root.left)
        # traverse right last
        self.pre_order3(current_root.right)

    def in_order(self):
        def traverse(root):
            # traverse left first
            if root.left:
                traverse(root.left)
            # operate on root second
            print(root.value)
            # traverse right last
            if root.right:
                traverse(root.right)
        traverse(self.root)

class BinarySearchTree(BinaryTree):
    def add(self, value):
        # find the correct spot to add this value and add it there
        pass

    def contains(self,value):
        # return true if the value is in the tree or false otherwise
        pass


if __name__ == "__main__":
    # Set a as root
    # set left of a to b
    # set the right of a to c


    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    b.left = d
    b.right = e
    c.left = f
# Option 1
    # tree = BinaryTree()

    # a.left = b
    # a.right = c
    # tree.root = a

# Option 2
    tree = BinaryTree(Node("A"))
    tree.root.left = b
    tree.root.right = c
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
    # print(tree.root.left.left.value)
    tree.in_order()
    tree.pre_order()
