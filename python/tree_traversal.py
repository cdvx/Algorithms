"""Tree traversal techniques implemented in python"""

__author__ = 'cdvx'

from binary_tree import my_tree

from binarytree import Node

my_other_tree = Node(1) 
my_other_tree.left = Node(2) 
my_other_tree.right = Node(3) 
my_other_tree.left.left = Node(4) 
my_other_tree.left.right = Node(5)


def in_order_traversal(my_tree: Node, tree_list: list =[]) -> None:
    if my_tree:
        in_order_traversal(my_tree.left)
        tree_list.append(my_tree.value)

        # print(my_tree.value)

        in_order_traversal(my_tree.right)
    print(tree_list)

def post_order_traversal(my_tree: Node, tree_list: list=[]) -> None:

    if my_tree:
        post_order_traversal(my_tree.left)

        post_order_traversal(my_tree.right)
        tree_list.append(my_tree.value)
        # print(my_tree.value)
    print(tree_list)

def pre_order_traversal(my_tree: Node, tree_list: list=[]) -> None:
    
    if my_tree:
        # print(my_tree.value)
        tree_list.append(my_tree.value)
        pre_order_traversal(my_tree.left)

        pre_order_traversal(my_tree.right)

    print(tree_list)


if __name__ == '__main__':

    print(my_tree)
    print(my_other_tree)

    print('>>>>>>>>in order>>>>>>>>', end='\n')

    # in_order_traversal(my_tree)
    in_order_traversal(my_other_tree)

    print('>>>>>>>>post order>>>>>>>>', end='\n')

    # post_order_traversal(my_tree)
    post_order_traversal(my_other_tree)

    print('>>>>>>>>pre order>>>>>>>>', end='\n')

    # pre_order_traversal(my_tree)
    pre_order_traversal(my_other_tree)
