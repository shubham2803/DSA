# Activity: 7.6.1 Building a Parse Tree (parsebuild)
# https://runestone.academy/ns/books/published/pythonds/Trees/ParseTree.html

from stack.stack_class import Stack
from class_tree1 import BinaryTree


def build_parse_tree(equation):
    equation = equation.split(' ')

    stack = Stack()
    new_node = BinaryTree('')
    stack.push(new_node)
    current_node = new_node

    for ele in equation:
        if ele == '(':
            current_node.insert_left('')
            stack.push(current_node)
            current_node = current_node.get_left_child()

        elif ele in ['+', '*', '-', '/', '//']:
            current_node.root = ele
            current_node.insert_right('')
            stack.push(current_node)
            current_node = current_node.right_child
        # test
        elif ele == ')':
            current_node = stack.pop()
        else:
            current_node.root = ele
            current_node = stack.pop()

    return new_node


build_parse_tree('( ( 3 + ( 4 * 5 ) ) + ( ( 10 + 5 ) * 3 )')


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root())
        inorder(tree.get_right_child())


def preorder(tree):
    if tree:
        print(tree.get_root())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


inorder(build_parse_tree('( ( 3 + ( 4 * 5 ) ) + ( ( 10 + 5 ) * 3 )'))
