class BinaryTree:
    def __init__(self, root=None, values=None):
        self.root = root
        # add values later

def pre_order(self, action=None):
    new_list = []
    def traverse(root, action):

        if not root:
            return

        action(root.value)
        traverse(root.left, action)
        traverse(root.right, action)
    
    traverse(self.root, action or print)

'actual = ['root', 'left, 'right']'

def test_pre_order(tiny):
    actual = []
    tiny.pre_order(actual.append)
    expected = ['root', 'left', 'right']
   

    #     root
    #   /     \
    # left    right



    @pytest.fixture
    def tiny()
        tree = BinaryTree()
        tree.add('root')
        tree.add('left')
        tree.add('right')
    return tree    