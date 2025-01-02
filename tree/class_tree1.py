class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left_child: BinaryTree | None = None
        self.right_child: BinaryTree | None = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_node = BinaryTree(new_node)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            new_node = BinaryTree(new_node)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root

    @classmethod
    def preorder(cls, tree):
        if tree:
            print(tree.get_root())
            cls.preorder(tree.get_left_child())
            cls.preorder(tree.get_right_child())

    def pre_order(self):
        print(self.root)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()
