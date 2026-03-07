class user:
    def __init__(self, username, email, name):
        self.username = username
        self.name = name
        self.email = email
        print("user successfully created")

    def introduce_yourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {} .".format(guest_name, self.name, self.email))

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
    

ridwan = user('ridwan','ridwan@gmail.com','ridwan abdul')
inaya = user('inaya','inaya@gmail.com','inaya muhammad')
abdulmaleek = user('abdulmaleek','abdulmaleek@gmail.com','abdulmaleek abdulrahman')
balkisu = user('balkisu','balkisu@gmail.com','balkisu bilal')
kafaya = user('kafaya','kafaya@gmail.com','kafaya abdulkareem')
walex = user('walex','walex@gmail.com','walex hakeem')
halima = user('halima','halima@gmail.com','halima quadri')
xana = user('xana', 'xana@gmail.com', 'xana')
sonia = user('sonia', 'sonia@gmail.com', 'sonia')
halima = user('halima', 'halima@gmail.com', 'halima')


users = [ridwan, inaya, abdulmaleek, balkisu, kafaya, walex, halima, xana, sonia]

print(users)

# user1 = user('john','johndoe@gmail.com', 'john doe')
# user2 = user('mary','maryjane@gmail.com', 'mary jane')
# print(user1.username, user1.email, user1.name)
# print(user1.introduce_yourself('David'))
# print(user2.name)

# Here we're writing a class to test class methods insert, find, update and list_all.

class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        if target is None:
            raise ValueError(f"user '{user.username}' not found")
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users
    

database = UserDatabase()

database.insert(ridwan)
database.insert(inaya)
database.insert(abdulmaleek)
database.insert(halima)

found_user = database.find('ridwan')
database.update(user('ridwan','ridwan@gmail.com','ridwan abdul'))
print(found_user)
print(database.list_all())

# This function turns the tuple to a tree NB: Not only tuples
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



#%%time  Here we're trying to analyze the algorithms complexity and identify inefficiencies
# import time

# start = time.time()

# for i in range(100000000):
#     j = i * i

# end = time.time()
# print("Elapsed:", end - start, "seconds")

    # We expect this function to return the total time it took to execute the iterations....

#here we're building a binary tree, continuation from the files binary_search_tree and sample_tree....
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Level 0
tree = BSTNode(ridwan.username, ridwan)
print(tree.key, tree.value) # View Level 0

# Level 1
tree.left = BSTNode(balkisu.username, balkisu)
tree.right = BSTNode(walex.username, walex)
print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)# View Level 1
print(display_keys(tree))

'''
QUESTION 11: Write a function to insert a new node into a BST.

We use the BST-property to perform insertion efficiently:

Starting from the root node, we compare the key to be inserted with the current node's key
If the key is smaller, we recursively insert it in the left subtree (if it exists) or attach it as as the left child if no left subtree exists.
If the key is larger, we recursively insert it in the right subtree (if it exists) or attach it as as the right child if no right subtree exists.
'''

#Here's a recursive implementation of insert

def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, ridwan.username, ridwan)
insert(tree, balkisu.username, balkisu)
insert(tree, walex.username, walex)
insert(tree, abdulmaleek.username, abdulmaleek)
insert(tree, kafaya.username, kafaya )
insert(tree, sonia.username, sonia)
insert(tree, xana.username, xana)
insert(tree, halima.username, halima)
print(display_keys(tree))

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)
    
node = find(tree, 'kafaya')
print(node.key, node.value)

'''
### Updating a value in a BST

> **QUESTION 12:** Write a function to update the value associated with a given key within a BST

We can use `find` to locate the node to be updated, and simply update it's value.
'''

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

update(tree, 'kafaya', user('kafaya', 'kafaya A', 'kafayaj@example.com'))
node = find(tree, 'kafaya')
print(node.value)

'''
### List the nodes

> **QUESTION 13:** Write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys.

The nodes can be listed in sorted order by performing an inorder traversal of the BST.
'''

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

print(list_all(tree))
# Here we're analysing the time complexity of the function above
import time

from sample_tree import tree_size

start = time.perf_counter()

for i in range(len(list_all(node))):
    j = i * i

end = time.perf_counter()
print("Elapsed:", end - start, "seconds")

'''
## Balanced Binary Trees

> **QUESTION 14**: Write a function to determine if a binary tree is balanced.

Here's a recursive strategy:

1. Ensure that the left subtree is balanced.
2. Ensure that the right subtree is balanced.
3. Ensure that the difference between heights of left subtree and right subtree is not more than 1.

'''

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return balanced, height

print(is_balanced(tree))

'''
## Balanced Binary Search Trees

> **QUESTION 15**: Write a function to create a balanced BST from a sorted list/array of key-value pairs.

We can use a recursive strategy here, turning the middle element of the list into the root, and recursively creating left and right subtrees.
'''

def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
    
data = [(user.username, user) for user in users]
print(data)
tree = make_balanced_bst(data)
print(display_keys(tree))
print(is_balanced(tree))

'''
## Balancing an Unbalanced BST

> **QUESTION 16:** Write a function to balance an unbalanced binary search tree.

We first perform an inorder traversal, then create a balanced BST using the function defined earlier.
'''
def balance_bst(node):
    return make_balanced_bst(list_all(node))
tree1 = None

for user in users:
    tree1 = insert(tree1, user.username, user)

print(display_keys(tree1))
tree2 = balance_bst(tree1)
print(display_keys(tree2))

'''
## A Python-Friendly Treemap 

We are now ready to return to our original problem statement.

> **QUESTION 1**: As a senior backend engineer at Jovian, you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users. It should allow the following operations to be performed efficiently:
> 
> 1. **Insert** the profile information for a new user.
> 2. **Find** the profile information of a user, given their username
> 3. **Update** the profile information of a user, given their usrname
> 5. **List** all the users of the platform, sorted by username
>
> You can assume that usernames are unique. 



We can create a generic class `TreeMap` which supports all the operations specified in the original problem statement in a python-friendly manner.
'''

class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in list_all(self.root))
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)
    
print(users)
treemap = TreeMap()
print(treemap.display())

treemap['balkisu'] = balkisu
treemap['kafaya'] = kafaya
treemap['sonia'] = sonia

print(treemap.display())
print(treemap['kafaya'])

print(len(treemap))

treemap['halima'] = halima
treemap['inaya'] = inaya
treemap['ridwan'] = ridwan
treemap['walex'] = walex
treemap['abdulmaleek'] = abdulmaleek

print(treemap.display())

for key, value in treemap:
    print(key, value)

print(list(treemap))

treemap['ridwan'] = user(username='ridwan', name='ridwan o abdul', email='ridwan@example.com')
print(treemap['ridwan'])




