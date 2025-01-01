# Activity: 7.6.1 Building a Parse Tree (parsebuild)
# https://runestone.academy/ns/books/published/pythonds/Trees/ParseTree.html

from stack.stack_class import Stack
from class_tree1 import BinaryTree


def build_parse_tree(equation):
    equation = equation.split()

    stack = Stack()
    new_node = BinaryTree('')
    stack.push(new_node)
    current_node = new_node

    for ele in equation:
        if ele == '(':
            current_node.left_child = BinaryTree('')
            current_node = current_node.left_child
            stack.push(current_node)

        elif ele in ['+', '*', '-', '/', '//']:
            current_node.root = ele
            current_node.right_child = BinaryTree('')
            current_node = current_node.right_child

        elif ele == ')':
            current_node = stack.pop()
        else:
            current_node.root = ele
            current_node = stack.pop()

    return new_node


print(build_parse_tree('(3+(4*5))'))
