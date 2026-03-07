'''
MERGE SORT

We'll focus on solving the following problem:

Question 1: You're working on a new feature on jovian called 'Top Notebooks of the week'. Write a function to sort a list of notebooks in decreasing order of likes. Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.


The problem of sorting a list of objects comes up over and over in computer science and software development, and it's important to understand common approaches for sorting and the trade-offs they offer, Before we solve the above problem, we'll solve a simplified version of the problem:

Question 2: Write a program to sort a list of numbers

'Sorting' usually refers to 'sorting in ascending order', unless specified otherwise.

The Method

Here's a systematic strategy we'll apply for solving problems:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
"Applying the right technique" is where the knowledge of common data structures and algorithms comes in handy.

Solution:

We need to write a function to sort a lsit of numbers in increasing order.

Input
1. nums: A list of numbers e.g [4, 2, 6, 3, 4, 6, 2, 1]

Output
2. sorted_nums: The sorted version of nums e.g [1, 2, 2, 3, 4, 4, 6, 6]

The signature of our function would be as follows:

def sort(nums):
    pass
    
'''
   
# List of numbers in random order
test0 = {
    'input' : {
        'nums' : [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output' : [1,2, 2, 3, 4, 4, 6, 6,]
}
# List of numbers in random order
test1 = {
    'input' : {
        'nums' : [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    },
    'output' : [-243, -12, 0, 1, 2, 5, 6, 7, 12, 23]
}
# A list that's already sorted 
test2 = {
    'input' : {
        'nums' : [3, 5, 6, 7, 8, 9, 10, 99]
    },
    'output' : [3, 5, 6, 7, 8, 9, 10, 99]
}
# A list that's sorted in descending order 
test3 = {
    'input' : {
        'nums' : [99, 10, 9, 8, 7, 6, 5, 4, 3]
    },
    'output' : [99, 10, 9, 8, 7, 6, 5, 4, 3]
}
# A list containing repeating element 
test4 = {
    'input' : {
        'nums' : [5, -12, 2, 6, 1, 23, 7, 7, -12, 6, 12, 1, -243, 1, 0]
    },
    'output' : [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]
}
# An empty list 
test5 = {
    'input' : {
        'nums' : []
    },
    'output' : []
}
# A list containing just one element 
test6 = {
    'input' : {
        'nums' : [23]
    },
    'output' : [23]
}
# A list containing one element repeated many times 
test7 = {
    'input' : {
        'nums' : [42, 42, 42, 42, 42, 42, 42]
    },
    'output' : [42, 42, 42, 42, 42, 42, 42]
}

# To create the final test case(a really long list), we can start with a sorted list created using `range` and shuffle it to create the input.

import random

in_list = list(range(10000))
out_list = list(range(10000))
random.shuffle(in_list)

test8 = {
    'input' : {
        'nums' : in_list
    },
    'output' : out_list
}

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]
# print(in_list[:10])
# print(out_list[:10])

'''
To state our solution in plain english:
1. Iterate over the list of numbers, starting from the left. 
2. Compare each number with the number that follows it.
3. If the number is greater than the one that follows it, swap the two elements.
4. Repeat steps 1 to 3 till the list is sorted. 

We need to repeat steps 1 to 3 at most n-1 times to ensure that the array is sorted. Can you
explain why? Hint: After one iteration, the largest number in the list.

This method is called bubble sort, as it causes smaller elements to bubble to the top and larger to sink at the bottom.
'''
# To implement we need to create a copy of the list inside our function, to avoid changing it while sorting.
def bubble_sort(nums):
    # Create a copy of the list to avoid changing it however it's not always necessary to always make a copy of the list.
    nums = list(nums)

    # 4. Repeat the process n-1 times 
    for j in range(len(nums)):

        # 1. Iterate over the array (except last element):
        for i in range(len(nums) - 1):

            # 2. Compare the number with
            if nums[i] > nums[i+1]:

                  # 3. Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]

    # Return the sorted list
    return nums

# This is the classical textbook bubble sort algorithm below

# def bubble_sort(nums):
#     nums = nums[:]   
#     n = len(nums)

#     for j in range(n):
#         for i in range(n - 1):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]

#     return nums

# This is a common way to swap values in python
x, y = 2, 3
x, y = y, x
print(x, y)

# Lets test the above function with an example
nums0 , output0 = test0['input']['nums'], test0['output']

print('input:', nums0)
print('Expected output:', output0)

result0 = bubble_sort(nums0)

print('Actual output;', result0)
print('Match;', result0 == output0)

# This function helps to reduce the length of list for display
def reduce_list_lenth(lst):
    # Return only first 10 items for display
    return lst[:15] if len(lst) > 15 else lst
 

if __name__ == "__main__":
    for t in (tests):
        nums = t['input']['nums']
        expected = t['output']
        # Actual = t[]
        result = bubble_sort(nums)
        print(f"nums={reduce_list_lenth(nums)}, result={reduce_list_lenth(result)}, expected={reduce_list_lenth(expected)}")
        import time
        start = time.time()
        result = bubble_sort(nums)
        end = time.time()
        print("Execution time", end - start)

# HURRAY!!! All our test cases above passed

'''
INSERT SORT

It's a simple sorting technique called insertion sort, where we keep the initial portion of the array sorted and insert the remaining elements one by one at the right position.
'''

# def insertion_sort(nums):
#     # Make a copy of the input to avoid mutating the original list
#     nums = list(nums)

#     # Loop through each index in the list
#     for i in range(len(nums)):
#         # Remove the current element we want to insert into the sorted portion
#         cur = nums.pop(i)

#         # Start comparing from the element just before the removed position
#         j = i - 1  

#         # Move backward while elements are greater than 'cur'
#         # This finds the correct insertion position
#         while j >= 0 and nums[j] > cur:
#             j -= 1

#         # Insert 'cur' into the position after the last element <= cur
#         nums.insert(j + 1, cur)

#     return nums


# Below is the classical textbook insertion sort and how it works:
def insertion_sort(nums):
    # Make a copy so the original list is not modified
    nums = list(nums)

    # Start from index 1 because index 0 is already "sorted"
    for i in range(1, len(nums)):
        key = nums[i]          # Element to insert
        j = i - 1              # Compare backward with sorted portion

        # Shift elements to the right until the correct position is found
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        # Insert key into the correct position
        nums[j + 1] = key

    return nums

# How This Version Works
# Step 1: Take the next element (key)
# Step 2: Move backward through the sorted part
# Step 3: Shift elements until finding the right location
# Step 4: Insert key in sorted order

# This avoids using pop() and insert(), which shift the list every time.

nums0, output0 = test0['input']['nums'], test0['output']

print('input:', nums0)
print('Expected output:', output0)

result0 = insertion_sort(nums0)

print('Actual output:', result0)
print('Match:', result0 == output0)

'''
Exercise

1. Read the source code of `insertion_sort` function and describe the algorithm in plain english. Reading the source code is an essential skill for software development.
2. Determine the time and space complexity of insertion sort. Is it any better than any bubble_sort? why or why not? 
'''
# SOLUTION:

# 1. Make a copy of the input to avoid mutating the original list
# 2. Loop through each index in the list
# 3. Remove the current element we want to insert into the sorted portion
# 4. Start comparing from the element just before the removed position
# 5. Move backward while elements are greater than 'cur'
# 6. Finds the correct insertion position
# 7. Insert 'cur' into the position after the last element <= cur

'''
DIVIDE AND CONQUER

To perform sorting more efficiently , we'll apply a strategy called divide and conquer, which has the following general steps:

1. Divide the inputs into two roughly equal parts.
2. Recursively solve the problem individually for each of the two parts.
3. Combine the results to solve the problem for the original inputs.
4. Include terminating conditions for small or indivisible inputs.

MERGE SORT ALGORITHM

Here's a step by step description for merge sort:
1. If the input list is empty or contains just one element, it is already sorted. Return it.
2. If not, divide the list of numbers into two roughly equal parts.
3. Sort each part recursively using the merge sort algorithm. You'll get back two sorted lists.
4. Merge the two sorted lists to get a single sorted list.
'''

# Question 3: Write a function to merge two sorted arrays.

def merge(left, right):
    # Merge two sorted lists into a single sorted list
    merged = []
    i = j = 0
    
    # Compare elements from left and right, add smaller one to merged
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add remaining elements from left
    merged.extend(left[i:])
    
    # Add remaining elements from right
    merged.extend(right[j:])
    
    return merged

# Lets implement the merge sort algorithm assuming we already have a helper function called `merge` for merging two sorted arrays.

def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint 
    mid = len(nums) // 2

    # Split the list into two halves 
    left = nums[:mid]
    right = nums[mid:]

    # Solve the problems for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)

    # Combine the results of the two halves
    sorted_nums = merge(left_sorted, right_sorted)

    return sorted_nums

# Lets try out the merge operation, before we test merge sort.
print(merge([1, 4, 7, 9, 11], [-1, 0, 2, 3, 8, 12])) # Successful ✅ 

# We can now test the `merge_sort` function.

nums0, output0 = test0['input']['nums'], test0['output']

print('input:', nums0) # Successful ✅ 
print('Expected output:', output0) # Successful ✅ 

result0 = merge_sort(nums0)

print('Actual output:', result0) # Successful ✅ 
print('Match:', result0 == output0) # Successful ✅ 

if __name__ == "__main__":
    for t in (tests):
        nums = t['input']['nums']
        expected = t['output']
        # Actual = t[]
        result = merge_sort(nums)
        print(f"nums={reduce_list_lenth(nums)}, result={reduce_list_lenth(result)}, expected={reduce_list_lenth(expected)}")
        import time
        start = time.time()
        result = merge_sort(nums)
        end = time.time()
        print("Execution time", end - start)

# We'll add some print statements to our `merge_sort` and `merge_functions` to display the tree fo recursive function calls.

def merge(nums1, nums2, depth=0):
    # Merge two sorted lists into a single sorted list
    print(' '*depth, 'merge:' , nums1, nums2)
    merged = []
    i = j = 0
    
    # Compare elements from nums1 and nums2, add smaller one to merged
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Add remaining elements from nums1
    merged.extend(nums1[i:])
    
    # Add remaining elements from nums2
    merged.extend(nums2[j:])
    
    return merged

def merge_sort(nums, depth=0):
    # Terminating condition (list of 0 or 1 elements)
    print(' '*depth, 'merge_sort:', nums )
    if len(nums) < 2:
        return nums
    
    # Get the midpoint 
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth+1),
                 merge_sort(nums[mid:], depth+1),
                 depth+1)  

# Lets test out the function below
print(merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12]))

# Extensions and variations of merge sort:
# Counting inversions in an array
# K-way merge sort
# Merge sort and insertion sort hybrids

'''
QUICKSORT 

The fact that merge sort requires allocating additional space as large as the input itself makes it somewhat slow in practice because memory allocation is far more expensive than comparisons or swapping.

To overcome the space inefficiencies of merge sort, we'll study another divide-and-conquer based sorting algorithm called quicksort, which works as follows:

1. If the list is empty or has just one element, return it. It's already sorted.
2. Pick a random element from the list. This element is called a pivot.
3. Reorder the list so that all elements with values greater than the pivot come after it. This operation is called partitioning.
4. The pivot element divides the array into two parts which can be sorted independently by making a recursive call to quicksort.

'''
# Here's an implementation of quicksort, assuming we already have a helper function called `partition` which picks a pivot, partitions the array in place, and returns the position of the pivot element.

def quicksort(nums, start=0, end=None):
    #print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

# Here's an implementation of partition, which uses the last element of the list as a pivot
def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1

    # Initialize right and left pointers
    l, r = start, end-1

    # Iterate while they're apart
    while r > l :
        # print(" ", nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1

        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1

        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
        # print(' ', nums, l, r)
        # Place the pivot between the two parts.
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end

# Let's see the partition function in action:
ll = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(ll)
print(ll, pivot)

# Let's see quicksort in action
nums0, output0 = test0['input']['nums'], test0['output']

print('input:', nums0)
print('Expected output:', output0)
result0 = quicksort(nums0)
print('Actual output:', result0)
print('Match:', result0 == output0)

if __name__ == "__main__":
    for t in tests:
        nums = t['input']['nums']
        expected = t['output']
        result = quicksort(nums)
        print(f"nums={reduce_list_lenth(nums)}, Actual output={reduce_list_lenth(result)}, expected={reduce_list_lenth(expected)}")
        import time
        start = time.time()
        result = quicksort(nums)
        end = time.time()
        print("Execution time", end - start)

'''
Let's return to our original problem statement now.

Question 1: You're working on a new feature on jovian called 'Top Notebooks of the week'. Write a function to sort a list of notebooks in decreasing order of likes. Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.

First, we need to sort objects not just numbers, Also, we want to sort them in the descending order of likes. To achieve this, all we need is a custom comparison function to compare two notebooks. 
'''

# A class that captures basic information about notebooks.
class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

# Let's create some sample notebooks

nb0 = Notebook('Dynamic-programming', 'ridwan', 894)
nb1 = Notebook('Intro-to-ethical-hacking', 'halima', 941)
nb2 = Notebook('Cybersecurity', 'Aliyu', 891)
nb3 = Notebook('Devops', 'balkisu', 789)
nb4 = Notebook('content marketing', 'kafaya', 800)
nb5 = Notebook('social marketing', 'inaya', 894)
nb6 = Notebook('football', 'abdulmaleek', 785)
nb7 = Notebook('basketball', 'aliya', 555)
nb8 = Notebook('jigsaw', 'taiba', 678)
nb9 = Notebook('Ramadan', 'adnan', 345)

Notebooks = [nb0, nb1, nb2, nb3, nb4, nb5, nb6, nb7, nb8, nb9]

print(Notebooks)

# Next we'll define a custom function for comparing two notebooks. It will return the strings `lesser`, `equal` or `greater` to establish order between the two objects.

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'
    
# Note that we say `nb1` is greater than `nb2 if it has higher likes because we want to sort the notebooks in decreasing order of likes.

# Here is an implementation of merge sort which accepts a custom comparison function.
def default_comparison(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'
    
def merge_sort(objs, compare=default_comparison):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare),
                 merge_sort(objs[mid:], compare),
                 compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

sorted_notebooks = merge_sort(Notebooks, compare_likes )
print(sorted_notebooks) # Successful ✅

# The notebooks are now sorted by likes, since we have written a generic `merge_sort` function that works with any compare function, we can also use it to sort the notebooks by title.

def compare_titles(nb1, nb2):
    if nb1.title > nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title < nb2.title:
        return 'greater'
   

# Implementing a double comparison below

# def compare_titles(nb1, nb2):
#     key1 = (nb1.title, nb1.username)
#     key2 = (nb2.title, nb2.username)

#     if key1 < key2:
#         return 'lesser'
#     elif key1 > key2:
#         return 'greater'
#     else:
#         return 'equal'

# Another method below
def compare_titles(nb1, nb2):
    if nb1.title > nb2.title:
        return 'lesser'
    elif nb1.title < nb2.title:
        return 'greater'
    else:
        if nb1.username > nb2.username:
            return 'lesser'
        elif nb1.username < nb2.username:
            return 'greater'
        else:
            return 'equal'
    
merge_sort(Notebooks, compare_titles)
print(merge_sort(Notebooks, compare_titles)) # Successful ✅

