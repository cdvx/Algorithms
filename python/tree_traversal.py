"""Tree traversal techniques implemented in python"""

from binary_tree import my_tree

print(my_tree)

def in_order_traversal(my_tree, tree_list=[]):

    if my_tree:
        in_order_traversal(my_tree.left)
        tree_list.append(my_tree.value)

        print(my_tree.value)

        in_order_traversal(my_tree.right)
    print(tree_list)

def post_order_traversal(my_tree, tree_list=[]):

    if my_tree:
        post_order_traversal(my_tree.left)

        post_order_traversal(my_tree.right)
        tree_list.append(my_tree.value)
        print(my_tree.value)
    print(tree_list)

def pre_order_traversal(my_tree, tree_list=[]):
    
    if my_tree:
        print(my_tree.value)
        tree_list.append(my_tree.value)

        pre_order_traversal(my_tree.left)

        pre_order_traversal(my_tree.right)

    print(tree_list)


print('>>>>>>>>in order>>>>>>>>')

in_order_traversal(my_tree)

print('>>>>>>>>post order>>>>>>>>')

post_order_traversal(my_tree)

print('>>>>>>>>pre order>>>>>>>>')

pre_order_traversal(my_tree)
