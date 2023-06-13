# Define a class for the nodes
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Define a class for the tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)
        if self.root is None: # If the tree is empty, set the root as the new node
            self.root = new_node
        else: # Otherwise, start from the root and find the right position
            current = self.root
            while True:
                if val < current.val: # If the new value is smaller than the current node, go left
                    if current.left is None: # If there is no left child, insert the new node there
                        current.left = new_node
                        break
                    else: # If there is a left child, update the current node as the left child
                        current = current.left
                elif val > current.val: # If the new value is larger than the current node, go right
                    if current.right is None: # If there is no right child, insert the new node there
                        current.right = new_node
                        break
                    else: # If there is a right child, update the current node as the right child
                        current = current.right
                else: # If the new value is equal to the current node, do nothing (no duplicates allowed)
                    break

# Create an example tree with some values
tree = BinarySearchTree()
tree.insert(5)
tree.insert(4)
tree.insert(10)
tree.insert(8)
tree.insert(20)
tree.insert(7)
print(type(tree))