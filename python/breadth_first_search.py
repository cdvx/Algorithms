"""Breadth first search implemented in python"""

__author__ = 'cdvx'

from binarytree import Node
# from tree_traversal import my_other_tree, my_tree
from queue import Queue


new_tree = Node(10)
new_tree.left = Node(20)
new_tree.right = Node(30)
new_tree.left.left = Node(40)
new_tree.left.right = Node(60)

def breadth_first_traversal(my_tree: Node) -> None:
    queue = Queue()
    x = []
    queue.put(my_tree)

    while not queue.empty():
        current_node = queue.get()
        x.append(current_node.value)

        if current_node.left:
            queue.put(current_node.left)

        if current_node.right:
            queue.put(current_node.right)
    return x
    

print('\n >>my_ this', new_tree)

    # breadth_first_traversal(my_other_tree)
print(breadth_first_traversal(new_tree))
    # print_level(new_tree)