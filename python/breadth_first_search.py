"""Breadth first search implemented in python"""

__author__ = 'cdvx'

from binarytree import Node
from tree_traversal import my_other_tree, my_tree

new_tree = Node(10)
new_tree.left = Node(20)
new_tree.right = Node(30)
new_tree.left.left = Node(40)
new_tree.left.right = Node(60)

def breadth_first_traversal(my_tree: Node, tree_list: list=[]) -> None:
    
    if my_tree:
        # print(my_tree.value)
        if my_tree.height == 0: return
        tree_list.extend([{"height": my_tree.height, "value":my_tree.value, "children":[my_tree.left, my_tree.right]}])
        
        breadth_first_traversal(my_tree.left)

        breadth_first_traversal(my_tree.right)

    return tree_list


def print_level(my_tree: Node) -> None:

    for i in range(0,my_tree.height+1):
        print_given_level(my_tree, i)

def print_given_level(my_tree: Node, level: int) -> None:
    # if my_tree is None: return 
    if level == 1:
        print(f'\n level >> {my_tree.value}')
    elif level > 1:
        print_given_level(my_tree.left, level-1)
        print_given_level(my_tree.right, level-1)


if __name__ == '__main__':
    # print(my_other_tree)
    print(my_tree)

    # breadth_first_traversal(my_other_tree)
    print(breadth_first_traversal(my_tree))
    # print_level(new_tree)