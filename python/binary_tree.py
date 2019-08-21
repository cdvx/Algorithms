__author__ = 'cdvx'

from binarytree import bst, tree, heap

# Generate a random binary tree and return its root node
my_tree = tree(height=3, is_perfect=False)

# Generate a random BST and return its root node
my_bst = bst(height=3, is_perfect=True)

# Generate a random max heap and return its root node
my_heap = heap(height=3, is_max=True, is_perfect=False)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value
        
    def getChildren(self):
        children = []
        if(self.left != None):
            children.append(self.left)
        if(self.right != None):
            children.append(self.right)
        return children

    def __str__(self):
        return str(self.value)
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = Node(value)

    def insert(self, value):
        self.set_root(value) if self.root is None\
            else self.insert_node(self.root, value)


    def insert_node(self, current_node, value):
        if value<= current_node.value :
            if current_node.left:
                self.insert_node(current_node.left, value)
            else:
                current_node.left = Node(value)
        elif value> current_node.value:
            if current_node.right :
                self.insert_node(current_node.right, value)
            else:
                current_node.right = Node(value)

    def find(self, value):
        return self.find_node(self.root, value)

    def find_node(self, current_node, value):
        if current_node is None:
            return False
        elif value == current_node.value:
            return True
        elif value < current_node.value:
            return self.find_node(current_node.left, value)
        else:
            return self.find_node(current_node.right, value)

    # def __str__(self):
    #     tree = []
    #     current = self.root
    #     count = 0
    #     if current is not None:
    #         count +=1
    #         node_dict = {'root': current} if count == 1 else {f'{count}': current}
    #         tree.append(node_dict)
    #         if current.left:
    #             tree[tree.index(node_dict)]['left'] = current.left
    #         if current.right:
    #             tree[tree.index(node_dict)]['right'] = current.right
    #         current = current.left if current.left else current.right
    #     return tree.__str__()


bst = BinarySearchTree()
bst.insert(23)
bst.insert(50)
bst.insert(30)
print(bst)
