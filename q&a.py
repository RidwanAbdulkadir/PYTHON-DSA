
'''
What is the purpose of defining the functions __str__ and __repr__ within a class? How are the two functions different? Illustrate with some examples using the empty cells below.

ANSWER:
The purpose of defining the `__str__` and `__repr__` functions within a class is to provide a way to represent the objects of that class as strings. These methods are used for different purposes:

1. `__repr__`: This method is intended to provide an "official" string representation of the object that can be used for debugging and development. It should ideally return a string that, when passed to `eval()`, would recreate the object. If this is not possible, it should return a string that gives a clear and unambiguous representation of the object.

2. `__str__`: This method is intended to provide a "user-friendly" string representation of the object. It is used when you print the object or use `str()` on it. The output should be easy to read and understand for end-users.
'''
#use the code snippet below to illustrate the difference between __str__ and __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        # Human-readable - what you want users to see
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        # Unambiguous - what developers/debuggers should see
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)

print(str(p))      # Alice is 30 years old
print(repr(p))     # Person(name='Alice', age=30)

print(p)           # Uses __str__: Alice is 30 years old

#Generic code for DFS (Depth first serach)

def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)

##Generic code for BFS (Breadth first serach)

from collections import deque

def bfs(root):
    q = deque([root])
    while q:
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
