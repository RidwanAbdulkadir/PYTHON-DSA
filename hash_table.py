'''
Here we'll be creating python dictionaries from scratch using data structure called Hash table. Dictionaries in python are used to store key-value pairs. Keys are used to store and retrieve values. For example, here's a dictionary for storing and retrieving phone numbers using people's names. 
'''

from textwrap import indent
from typing import Self


phone_numbers = {
    'ridwan' : '48484848484',
    'halima' : '30303030303',
    'balkis' : '43434343434'

}
print(phone_numbers['ridwan'])

# Add a value
phone_numbers['walex'] = '12121212121'
#update existing value
phone_numbers['ridwan'] = '11111111111'
print(phone_numbers)

# We can also view all the names and phone numbers stored in phone_numbers using a for loop.

for name in phone_numbers:
    print('Name:', name, 'Phone Number:', phone_numbers[name]) 

'''
TASK 1

Implement a HashTable class which supports the following operations:
1. Insert: Insert a new key-value pair
2. Find: Find the value associated with a key
3. Update: Update the value associated with a key
4. List: List all the keys stored in the hash table

The HashTable class will have the following structure(note the function signatures):
'''

class HashTable:
    def insert(self, key, value):
        ''' Insert a new key-value pair'''
        pass

    def find(self, key):
        '''Find the value associated with a key'''
        pass

    def update(self, key, value):
        '''Change the value associated with a key'''
        pass

    def list_all(self):
        '''List all the keys'''
        pass



'''
We'll build a HashTable class step by step. As a first step is to create a python list which will hold all the key-value pairs. We'll start by creating a list of a fixed size.
'''

MAX_HASH_TABLE_SIZE = 4096

#QUESTION 1: Create a Python list of size MAX_HASH_TABLE_SIZE, with all the values set to None.

# List of size MAX_HASH_TABLE_SIZE with all values None
data_list = [None] * 4096
# print(data_list)
print(len(data_list))

# TEST CASES: if the list was created successfully, the code below should output True.

len(data_list) == 4096
print(len(data_list))
data_list[99] == None 
print(data_list[99])

#using a loop to try out the test cases

for item in data_list:
    assert item == None # assert function throws an error when something is wrong with our code and test cases.

'''
Hashing Function

A hashing function is used to convert strings and other non-numeric data types into numbers, which can then be used as list indices. For instance, if a hashing function converts the string 'ridwan' into the number `4`, then the key-value pair ('ridwan' : '48484848484') will be stored at the position `4` within the data list. 

A simple algorithm for hashing, which can convert strings into numeric list indices.
1. Iterate over the string, character by character
2. Convert each character to a number using python's built-in ord function
3. Add the numbers for each character to obtain the hash table for the entire string 
4. Take the remainder of the result with the size of the data list 
'''
print(ord('x'))
#QUESTION 2: Complete the get_index function below which implements the hashing algorithms described above.

def get_index(data_list, a_string):
    # variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        #convert the character to a number (using ord)
        a_number = ord(a_character)
        # update the result by adding the number 
        result += a_number

    # Take the remainder of the result with the size of the data list
    list_index = result  % len(data_list)
    return list_index

# def get_index(data_list, key):
#     idx = hash(key) % len(data_list)

#     while True:
#         kv = data_list[idx]

#         # slot is empty → use it
#         if kv is None:
#             return idx
        
#         # same key found → reuse slot
#         if kv[0] == key:
#             return idx

#         # linear probing
#         idx = (idx + 1) % len(data_list)

# If the get_index  was defined properly the code below should output True.
get_index(data_list, '') == 0
print(get_index(data_list, ''))
print(get_index(data_list, 'ridwan')) == 645
print(ord('r') + ord('i') + ord('d') + ord('w') + ord('a') + ord('n'))
print(645 % 4096) #function gets the remainder

'''
INSERT
To insert a key-value pair into a hash table, we can simply get the hash of the key, and store the pair at that index in the data list. 
'''

key, value = 'ridwan', '11111111111'
idx = get_index(data_list, key)
print(idx)

data_list[idx] = (key, value) # we can use this line of code to save the key, value in our desired index

# Here's the same operation expressed in a single line of code.
data_list[get_index(data_list, 'ridwan')] = ('ridwan', '11111111111')
print(data_list[get_index(data_list, 'ridwan')])

'''
FIND
To retrieve the value associated with a pair, we can get the hash of the key and look up that index in the data list.
'''

idx = get_index(data_list, 'ridwan')
print(idx)
key, value = data_list[idx]
print(value)

'''
LIST
To get the list of keys, we can simply use a list comprehension.
'''
# list1 = [1, 2, 3, 4, 7, 9, 11]
# # list2 = [ x for x in list1] #this scenario is the same with the one below just that the below will multiply by 2
# # # list2 = [ x *2 for x in list1] #multiply by 2
# # list2 = [ x *x for x in list1] ##multiply by itself
# import math
# list2 = [ math.ceil(x) for x in list1 if x > 5] #round up numbers to the nearest one,the condition at the end is also obeyed
# print(list2)

pairs = [kv[0] for kv in data_list if kv is not None]
print(pairs)

'''
Basic Hash Table Implementation
use the function above to implement a basic hash table in python
Question 3: Complete the hash table implementation below by following the instructions in the comment.
Hint: insert and update can have identical implementations.
'''

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size max_size with all values None
        self.data_list = [None] * max_size

    def insert(self,key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key) 
                        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
        
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [ kv[0] for kv in self.data_list if kv is not None]
    

# If the BasicHashTable class was defined correctly, the following code should output True.

basic_table = BasicHashTable(max_size=1024)
print(len(basic_table.data_list) == 1024) # successful✅

#insert some values
basic_table.insert('halima', '11111111111')
basic_table.insert('kafaya', '22222222222')

#Find a value
basic_table.find('halima') == '11111111111'
basic_table.find('kafaya') == '22222222222'
print(basic_table.find('halima') == '11111111111') # successful✅
print(basic_table.find('kafaya') == '22222222222') # successful✅

# Update a value
basic_table.update('halima', '33333333333')

# Check the updated value
basic_table.find('halima') == '33333333333'
print(basic_table.find('halima') == '33333333333') # successful✅

# Get the list of keys
basic_table.list_all() == ['halima', 'kafaya']
print(basic_table.list_all() == ['halima', 'kafaya']) # successful✅

'''
Handling Collision with Linear Probing
Multiple keys can have the same hash. For instance, the keys `listen` and `silent` have the same hash. This is referred to as collision. Data stored against one key may override the data stored against another, if they have the same hash.
'''

get_index(data_list, 'listen'), get_index(data_list, 'silent')
print(get_index(data_list, 'listen'), get_index(data_list, 'silent')) # successful✅

'''
To handle collisions we'll use a technique called linear probing. Here's how it works:
1. While inserting a new key-value pair if the target index for a key is occupied by another key, then we try the next index, followed by the next and so on till we get to the closest location.
2. While finding a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for a location which contains a key-value pair with the matching key.
3. While updating a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for a location which contains a key-value pair with the matching key, and update its value.

We'll define a function called `get_valid_index`, which starts searching the data list from the index determined by the hashing function `get_index` which returns the first index which is either empty or contains a key-value pair matching the given key.
'''
# Question 4: Complete the function `get_valid_index` below by following the instructions in the comments.

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx 
        
        # Move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

# If get_valid_index was defined correctly, the following cells should output True.

# Create an empty hash table
data_list2 = [None] * MAX_HASH_TABLE_SIZE

# New key `listen` should return expected index
get_valid_index(data_list2, 'listen') == 655
print(get_valid_index(data_list2, 'listen') == 655) # successful✅

# Insert a key-value pair for the key 'listen'
data_list2[get_index(data_list2, 'listen')] = ( 'listen', 99)


# Colliding key 'silent' should return next index
get_valid_index(data_list2, 'silent') == 656
print(get_valid_index(data_list2, 'silent') == 656) # successful✅


'''
Hash Table with Linear Probing

QUESTION 5: Complete the hash table (with linear probing) implementation below by following the instructions in the comments.
'''
MAX_HASH_TABLE_SIZE = 4096

class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size max_size with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value

    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]

    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)

        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]
    
# The following code should return `True` if the class above is well defined.

# Create a new hash table
probing_table = ProbingHashTable()
print(len(probing_table.data_list)) # Successful✅

# Insert a value
probing_table.insert('listen', 99)

# Check the value
probing_table.find('listen') == 99
print(probing_table.find('listen') == 99) # Successful✅

# Insert a colliding key
probing_table.insert('silent', 200)
print("TABLE NOW:",probing_table.data_list[650:670])  # Successful✅


# Check the new old keys
probing_table.find('listen') == 99 and probing_table.find('silent') == 200
print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200) # Successful✅

# Update a key 
probing_table.insert('listen', 101)

# Check the value
probing_table.find('listen') == 101
print(probing_table.find('listen') == 101) # Successful✅

probing_table.list_all() == ['listen', 'silent']
print(probing_table.list_all() == ['listen', 'silent']) # Successful✅
print("LIST_ALL:", probing_table.list_all()) # Successful✅

print("listen index:", get_valid_index(probing_table.data_list, 'listen')) # Successful✅
print("silent index:", get_valid_index(probing_table.data_list, 'silent')) # Successful✅

'''
Python Dictionaries using Hash Tables
python dictionaries can be implemented using hash tables. Also, Python provides a built-in function called `hash` which we can use instead of our custom hash function. It is likely to have far fewer collisions.
'''
# Question: Implement a python friendly interface for the hash table.

# MAX_HASH_TABLE_SIZE = 4096

class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        # Use python's built-in function to implement a linear probing hash table
        
        # Start with the index returned by get_index
        idx = hash(key) % len(self.data_list)

        while True:
            # Get the key-value pair stored at idx
            kv = self.data_list[idx]

            # If it is None, return the index
            if kv is None:
                return idx
            
            # If the stored key matches the given key, return the index
            k, v = kv
            if k == key:
                return idx 
            
            # Move to the next index
            idx += 1

            # Go back to the start if you have reached the end of the array
            if idx == len(self.data_list):
                idx = 0
            
    def __getitem__(self, key):
        # Implement the logic for find here
        idx = self.get_valid_index(key)

        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
        
    def __setitem__(self, key, value):
        # Implement the logic for 'insert/update' here
        # 1. Find the index for the key using get_valid_index
        idx = self.get_valid_index(key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)
        
    def __iter__(self):
        return iter(sorted(x for x in self.data_list if x is not None))

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(k), repr(v))) for k, v in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"
    

# If the `HashTable` class was defined correctly, the following code should output True.

# Create a hash table
table = HashTable()

# Insert some key-value pairs
table['a'] = 1
table['b'] = 34

# Retrieve the inserted values 
table['a'] == 1 and table['b'] == 34
print(table['a'] == 1 and table['b'] == 34)

# Update a value 
table['a'] = 99

# check the updated value 
table['a'] == 99
print(table['a'] == 99)

# Get a list of key-value pairs 
list(table) == [('a', 99), ('b', 34)]
print(list(table) == [('a', 99), ('b', 34)])
