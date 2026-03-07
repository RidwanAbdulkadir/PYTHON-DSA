class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)

print(node0)
print(node0.key)

node0.left = node1
node0.right = node2
tree = node0

print(tree.key)
print(tree.left.key)
print(tree.right.key)

# This function turns given data to a tuple 
def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree = parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

print(tree.left.left.key)
print(tree)

'''
Exercise: Define a function `tree_to_tuple` that converts a binary tree into a tuple representing the same tree. E.g. `tree_to_tuple` converts the tree created above to the tuple `((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))`. *Hint*: Use recursion.

'''
# This function turns a tree to tuple
def tree_to_tuple(node):
    
    if node is None:
        return None
    elif node.left is None and node.right is None:
        return node.key
    else:
        return (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))

# This function turns the tuple to a tree
def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

# Here we'll start looking into traversals python DSA

def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))
    
def traverse_pre_order(node):
    if node is None: 
        return []
    return( [node.key] + traverse_pre_order(node.left) + 
           traverse_pre_order(node.right))
    
def traverse_post_order(node):
    if node is None: 
        return []
    return(traverse_post_order(node.left) +  
           traverse_post_order(node.right) +  [node.key])

print(display_keys(tree, '  ')) 
print(tree_to_tuple(tree))
print(traverse_in_order(tree))
print(traverse_pre_order(tree))
print(traverse_post_order(tree))
        
# This function calculates the height and depth of a binary tree
def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree))

# Here's a function to count the number of nodes in a binary tree.
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

print(tree_size(tree))

'''
As a final step, let's compile all the functions we've written so far as methods withing the `TreeNode` class itself. Encapsulation of data and functionality within the same class is a good programming practice.
'''

class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)    
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

# Here I'm just trying a particular point in the tutorial that seems confusing...
tree_tuple = (((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(tree_tuple)
tree = TreeNode.parse_tuple(tree_tuple)
print(tree.traverse_in_order())