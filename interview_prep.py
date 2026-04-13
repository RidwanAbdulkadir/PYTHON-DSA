'''
The following question was asked during a coding interview for Amazon. The question is as follows:

Question: You are given an array of numbers(non-negative), Find a continous subarray of the list which adds up to a given sum.(Also return the index of the start and end of the subarray)

Example:
Input: arr = [1, 2, 3, 7, 5], sum = 12
Output: Subarray found from index 2 to 4
Explanation: The subarray [3, 7, 5] adds up to 12 and is found from index 2 to 4 in the given array.

Input: arr = [1, 2, 3, 4, 5], sum = 9
Output: Subarray found from index 1 to 3
Explanation: The subarray [2, 3, 4] adds up to 9 and is found from index 1 to 3 in the given array.
Input: arr = [1, 2, 3, 4, 5], sum = 15
Output: Subarray found from index 0 to 4
Explanation: The subarray [1, 2, 3, 4, 5] adds up to 15 and is found from index 0 to 4 in the given array.
Input: arr = [1, 2, 3, 4, 5], sum = 20
Output: No subarray found
Explanation: There is no subarray that adds up to 20.

provide solution using three approach:

1. Iteratively
2. Use Recursion
3. Memorization

'''

def find_subarray_with_sum(arr, target_sum):
    current_sum = 0 # Initialize current sum to 0
    start_index = 0 # Initialize start index to 0

    for end_index in range(len(arr)): # Iterate through the array using end_index
        current_sum += arr[end_index] # Add the current element to the current sum

        while current_sum > target_sum and start_index <= end_index: # If current sum exceeds target sum, move the start index to the right
            current_sum -= arr[start_index] # Subtract the element at start index from current sum
            start_index += 1 # Move the start index to the right

        if current_sum == target_sum: # If current sum equals target sum, return the indices of the subarray
            return f"Subarray found from index {start_index} to {end_index}" # Return the indices of the subarray that adds up to the target sum

    return "No subarray found"  # If no subarray is found that adds up to the target sum, return a message indicating that no subarray was found

# Test cases
arr1 = [1, 2, 3, 7, 5]
sum1 = 12
print(find_subarray_with_sum(arr1, sum1))  # Output: Subarray found from index 1 to 3

arr2 = [1, 2, 3, 4, 5]
sum2 = 9
print(find_subarray_with_sum(arr2, sum2))  # Output: Subarray found from index 1 to 3

arr3 = [1, 2, 3, 4, 5]
sum3 = 15
print(find_subarray_with_sum(arr3, sum3))  # Output: Subarray found from index 0 to 4

arr4 = [1, 2, 3, 4, 5]
sum4 = 20
print(find_subarray_with_sum(arr4, sum4))  # Output: No subarray found


def find_subarray_with_sum_recursive(arr, target_sum):
    def helper(start): # Define a helper function that takes the starting index as an argument
        if start >= len(arr): # If the starting index is greater than or equal to the length of the array, return a message indicating that no subarray was found
            return "No subarray found"
        current_sum = 0 # Initialize current sum to 0
        for end in range(start, len(arr)): # Iterate through the array starting from the given index
            current_sum += arr[end] # Add the current element to the current sum
            if current_sum == target_sum: # If the current sum equals the target sum, return the indices of the subarray
                return f"Subarray found from index {start} to {end}" # Return the indices of the subarray that adds up to the target sum
        return helper(start + 1) # If no subarray is found starting from the current index, recursively call the helper function with the next index
    return helper(0) # Call the helper function starting from index 0 to find the subarray that adds up to the target sum  

# Test cases
print(find_subarray_with_sum_recursive(arr1, sum1))  # Output: Subarray found from index 1 to 3

print(find_subarray_with_sum_recursive(arr2, sum2))  # Output: Subarray found from index 1 to 3

print(find_subarray_with_sum_recursive(arr3, sum3))  # Output: Subarray found from index 0 to 4

print(find_subarray_with_sum_recursive(arr4, sum4))  # Output: No subarray found

def find_subarray_with_sum_memoization(arr, target_sum):
    memo = {} # Initialize a dictionary to store previously computed results for subproblems
    def helper(start): # Define a helper function that takes the starting index as an argument
        if start in memo: # If the result for the current starting index is already computed and stored in the memoization dictionary, return the stored result
            return memo[start] # Return the stored result for the current starting index from the memoization dictionary
        if start >= len(arr): # If the starting index is greater than or equal to the length of the array, return a message indicating that no subarray was found
            return "No subarray found"
        current_sum = 0 # Initialize current sum to 0
        for end in range(start, len(arr)): # Iterate through the array starting from the given index
            current_sum += arr[end] # Add the current element to the current sum
            if current_sum == target_sum: # If the current sum equals the target sum, return the indices of the subarray
                result = f"Subarray found from index {start} to {end}" # Store the result in a variable before returning it
                memo[start] = result # Store the result for the current starting index in the memoization dictionary before returning it
                return result # Return the indices of the subarray that adds up to the target sum
        result = helper(start + 1) # If no subarray is found starting from the current index, recursively call the helper function with the next index and store the result in a variable before returning it
        memo[start] = result # Store the result for the current starting index in the memoization dictionary before returning it
        return result # Return the result of the recursive call to find the subarray that adds up to the target sum starting from the next index
    return helper(0) # Call the helper function starting from index 0 to find the subarray that adds up to the target sum using memoization   

# Test cases
print(find_subarray_with_sum_memoization(arr1, sum1))  # Output: Subarray found from index 1 to 3

print(find_subarray_with_sum_memoization(arr2, sum2)) # Output: Subarray found from index 1 to 3

print(find_subarray_with_sum_memoization(arr3, sum3)) # Output: Subarray found from index 0 to 4

print(find_subarray_with_sum_memoization(arr4, sum4)) # Output: No subarray found
print(find_subarray_with_sum( [3,1,2,5,7,8,9,1,12 ], 10)) # Output: No subarray found


'''
The following question was asked during a coding interview at google:

MINIMUM EDIT DISTANCE

Question: Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step). You have the following 3 operations permitted on a word:

i. Insert a character
ii. Delete a character
iii. Replace a character


'''

def min_steps(A, B):
    m = len(A) # Get the length of string A
    n = len(B) # Get the length of string B
    dp = [[0] * (n + 1) for _ in range(m + 1)] # Create a 2D list to store the minimum edit distance for each subproblem

    for i in range(m + 1): # Initialize the first column of the dp table
        dp[i][0] = i # The minimum edit distance to convert a string of length i to an empty string is i (delete all characters)

    for j in range(n + 1): # Initialize the first row of the dp table
        dp[0][j] = j # The minimum edit distance to convert an empty string to a string of length j is j (insert all characters)

    for i in range(1, m + 1): # Fill the dp table using dynamic programming
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]: # If the characters are the same, no operation is needed
                dp[i][j] = dp[i - 1][j - 1] # The minimum edit distance is the same as the previous subproblem
            else: # If the characters are different, consider all three operations and take the minimum
                dp[i][j] = min(dp[i - 1][j] + 1,      # Delete a character from A
                               dp[i][j - 1] + 1,      # Insert a character into A
                               dp[i - 1][j - 1] + 1) # Replace a character in A with a character from B

    return dp[m][n] # Return the minimum edit distance to convert A to B

# Test cases
A1 = "kitten"
B1 = "sitting"
print(min_steps(A1, B1))  # Output: 3

A2 = "flaw"
B2 = "lawn"
print(min_steps(A2, B2))  # Output: 2

A3 = "intention"
B3 = "execution"
print(min_steps(A3, B3))  # Output: 5

A4 = "abc"
B4 = "def"
print(min_steps(A4, B4))  # Output: 3


# Using Recursion
def min_steps_recursive(A, B):
    if not A: # If string A is empty, the minimum edit distance is the length of string B (insert all characters)
        return len(B)
    if not B: # If string B is empty, the minimum edit distance is the length of string A (delete all characters)
        return len(A)

    if A[0] == B[0]: # If the first characters of both strings are the same, no operation is needed
        return min_steps_recursive(A[1:], B[1:]) # Move to the next characters in both strings

    # If the first characters are different, consider all three operations and take the minimum
    return 1 + min(min_steps_recursive(A[1:], B),      # Delete a character from A
                   min_steps_recursive(A, B[1:]),      # Insert a character into A
                   min_steps_recursive(A[1:], B[1:])) # Replace a character in A with a character from B
 

# Test cases
A1 = "kitten"
B1 = "sitting"
print(min_steps_recursive(A1, B1))  # Output: 3

A2 = "flaw"
B2 = "lawn"
print(min_steps_recursive(A2, B2))  # Output: 2

A3 = "intention"
B3 = "execution"
print(min_steps_recursive(A3, B3))  # Output: 5

A4 = "abc"
B4 = "def"
print(min_steps_recursive(A4, B4))  # Output: 3 


# Using memorisation
def min_steps_memo(A, B):
    memo = {} # Initialize a dictionary to store previously computed results for subproblems
    def helper(i, j): # Define a helper function that takes the current indices of strings A and B as arguments
        if (i, j) in memo: # If the result for the current indices is already computed and stored in the memoization dictionary, return the stored result
            return memo[(i, j)] # Return the stored result for the current indices from the memoization dictionary
        if i == len(A): # If string A is empty, the minimum edit distance is the length of string B (insert all characters)
            return len(B) - j
        if j == len(B): # If string B is empty, the minimum edit distance is the length of string A (delete all characters)
            return len(A) - i

        if A[i] == B[j]: # If the current characters of both strings are the same, no operation is needed
            result = helper(i + 1, j + 1) # Move to the next characters in both strings and store the result in a variable before returning it
            memo[(i, j)] = result # Store the result for the current indices in the memoization dictionary before returning it
            return result # Return the minimum edit distance for the current indices

        # If the current characters are different, consider all three operations and take the minimum
        result = 1 + min(helper(i + 1, j),      # Delete a character from A
                         helper(i, j + 1),      # Insert a character into A
                         helper(i + 1, j + 1)) # Replace a character in A with a character from B and store the result in a variable before returning it
        memo[(i, j)] = result # Store the result for the current indices in the memoization dictionary before returning it
        return result # Return the minimum edit distance for the current indices
    return helper(0, 0) # Call the helper function with the initial indices (0, 0)

# Test cases
A1 = "kitten"
B1 = "sitting"
print(min_steps_memo(A1, B1))  # Output: 3

A2 = "flaw"
B2 = "lawn"
print(min_steps_memo(A2, B2))  # Output: 2

A3 = "intention"
B3 = "execution"
print(min_steps_memo(A3, B3))  # Output: 5

A4 = "abc"
B4 = "def"
print(min_steps_memo(A4, B4))  # Output: 3

###