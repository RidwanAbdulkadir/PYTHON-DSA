'''
RECURSION, MEMORIZATION AND DYNAMIC PROGRAMMING

Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

Memorization is an optimization technique used to speed up recursive algorithms by storing the results of expensive function calls and returning the cached result when the same inputs occur again. This can significantly reduce the time complexity of recursive algorithms.

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems, storing the results of those subproblems to avoid redundant work. It can be implemented using either a top-down approach (with recursion and memorization) or a bottom-up approach (iteratively filling a table).

Let's solve some problems using these techniques:

Longest Common Subsequence

QUESTION 1: Write a function to find the length of the longest common subsequence between two sequences. e.g Given the strings `serendipitous` and `precipitation`, the longest common subsequence is `reipito` which has a length of 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. For example, 'edpt' is a subsequence of "serendipitous". 

Approach: We are given two sequences, and we need to find the length of the longest common subsequence between them.

Input:
1. seq1: A sequence e.g `serendipitous`
2. seq2: Another sequence e.g `precipitation`

Output:
len_lcs: Length of the common subsequence e.g 7

Test cases

1. General case(string)
2. General case(list)
3. No common subsequence
4. One is a subsequence of the other 
5. One sequence is empty
6. Both sequences are empty
7. Multiple subsequences of the same length (abcdef and badcfe)
8. ???

Based on the above we can now create a signature of our function:

Recursive approach:
1. Create two counters idx1 and idx2 starting at 0. Our recursive function will compute LCS of seq1[idx1:] and seq2[idx2:]

2. if seq1[idx1] and seq2[idx2] are the same, then we can include this character in our LCS and move both counters forward by 1. So we return 1 + len_lcs(seq1, seq2, idx1 + 1, idx2 + 1)
'''

def len_lcs(seq1, seq2):
    return len_lcs_helper(seq1, seq2, 0, 0)

def len_lcs_helper(seq1, seq2, idx1, idx2):
    # Base cases
    if idx1 >= len(seq1) or idx2 >= len(seq2):
        return 0

    # If characters match, include this character in LCS
    if seq1[idx1] == seq2[idx2]:
        return 1 + len_lcs_helper(seq1, seq2, idx1 + 1, idx2 + 1)
    else:
        # If characters don't match, try both possibilities and take the maximum
        return max(len_lcs_helper(seq1, seq2, idx1 + 1, idx2), len_lcs_helper(seq1, seq2, idx1, idx2 + 1))
    
test0 = len_lcs("serendipitous", "precipitation") # Expected output: 7
test1 = len_lcs([1, 2, 3, 4], [2, 3, 4, 5]) # Expected output: 3
test2 = len_lcs("abc", "def") # Expected output: 0
test3 = len_lcs("abc", "abc") # Expected output: 3
test4 = len_lcs("", "abc") # Expected output: 0
test5 = len_lcs("", "") # Expected output: 0
test6 = len_lcs("abcdef", "badcfe") # Expected output: 3 (the longest common subsequences are "adf" and "bce")
test7 = len_lcs("AGGTAB", "GXTXAYB") # Expected output: 4 (the longest common subsequence is "GTAB")

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

if test0 == 7 and test1 == 3 and test2 == 0 and test3 == 3 and test4 == 0 and test5 == 0 and test6 == 3 and test7 == 4:
    print("All test cases passed!")
else:    print("Some test cases failed.")

if __name__ == "__main__":
    # You can add more test cases here
    test_cases = [
        ("serendipitous", "precipitation"),
        ([1, 2, 3, 4], [2, 3, 4, 5]),
        ("abc", "def"),
        ("abc", "abc"),
        ("", "abc"),
        ("", ""),
        ("abcdef", "badcfe"),
        ("AGGTAB", "GXTXAYB")
    ]
    import time
    for seq1, seq2 in test_cases:
        print(f"seq1: {seq1}, seq2: {seq2}")
        start = time.time()
        result = len_lcs(seq1, seq2)
        end = time.time()
        print(f"Result: {result}, Time taken: {end - start:.4f} seconds") # ✅ Successful

'''
MEMORIZATION APPROACH: It is a top-down approach where we store the results of previously computed subproblems in a dictionary (or any other data structure) to avoid redundant calculations. This can significantly reduce the time complexity from exponential to polynomial.

1. We can use a dictionary to store the results of subproblems, where the keys are tuples of (idx1, idx2) and the values are the lengths of the longest common subsequence for those indices.
2. Before performing the recursive calls, we check if the result for the current indices is already computed and stored in the dictionary. If it is, we return that value instead of recomputing it.
3. The rest of the logic remains the same as the recursive approach, but with the added benefit of avoiding redundant calculations, which can significantly improve performance for larger inputs.
4. The time complexity of this approach is O(m*n) and the space complexity is also O(m*n) due to the memoization dictionary storing results for each pair of indices.
'''
def lcs_memo(seq1, seq2):
    memo = {}
    def helper(idx1, idx2):
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        
        if idx1 >= len(seq1) or idx2 >= len(seq2):
            return 0
        
        if seq1[idx1] == seq2[idx2]:
            memo[(idx1, idx2)] = 1 + helper(idx1 + 1, idx2 + 1)
        else:
            memo[(idx1, idx2)] = max(helper(idx1 + 1, idx2), helper(idx1, idx2 + 1))
        
        return memo[(idx1, idx2)]
    
    return helper(0, 0)


if test0 == 7 and test1 == 3 and test2 == 0 and test3 == 3 and test4 == 0 and test5 == 0 and test6 == 3 and test7 == 4:
    print("All test cases passed!")
else:    print("Some test cases failed.")

if __name__ == "__main__":
    import time
    test_cases = [
        ("serendipitous", "precipitation"),
        ([1, 2, 3, 4], [2, 3, 4, 5]),
        ("abc", "def"),
        ("abc", "abc"),
        ("", "abc"),
        ("", ""),
        ("abcdef", "badcfe"),
        ("AGGTAB", "GXTXAYB")
    ]
    for seq1, seq2 in test_cases:
        print(f"seq1: {seq1}, seq2: {seq2}")
        start = time.time()
        result = lcs_memo(seq1, seq2)
        end = time.time()
        print(f"Result: {result}, Time taken: {end - start:.4f} seconds") # ✅ Successful

'''
DYNAMIC PROGRAMMING APPROACH: It is a bottom-up approach where we iteratively fill a table (usually a 2D array) based on the results of smaller subproblems. This approach typically has a time complexity of O(m*n) and space complexity of O(m*n), where m and n are the lengths of the two sequences.

1. We can use a 2D array to store the lengths of the longest common subsequence for each pair of indices.
2. We fill the table iteratively, starting from the base cases (empty sequences) and building up to the final solution.
3. The rest of the logic remains the same as the recursive approach, but with the added benefit of avoiding redundant calculations, which can significantly improve performance for larger inputs.
4. The time complexity of this approach is O(m*n) and the space complexity is also O(m*n) due to the 2D array storing results for each pair of indices.
'''
# def lcs_dp(seq1, seq2):
#     m, n = len(seq1), len(seq2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
    
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if seq1[i - 1] == seq2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
#     return dp[m][n]

# another attempt
def lcs_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    table = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]: 
                table[i + 1][j + 1] = 1 + table[i][j]
            else:
                table[i + 1][j + 1] = max(table[i][j], table[i + 1][j])
    return table[-1][-1]

if test0 == 7 and test1 == 3 and test2 == 0 and test3 == 3 and test4 == 0 and test5 == 0 and test6 == 3 and test7 == 4:
    print("All test cases passed!")
else:    print("Some test cases failed.")

if __name__ == "__main__":

    test_cases = [
        ("serendipitous", "precipitation"),
        ([1, 2, 3, 4], [2, 3, 4, 5]),
        ("abc", "def"),
        ("abc", "abc"),
        ("", "abc"),
        ("", ""),
        ("abcdef", "badcfe"),
        ("AGGTAB", "GXTXAYB")
    ]
    for seq1, seq2 in test_cases:
        print(f"seq1: {seq1}, seq2: {seq2}")
        start = time.time()
        result = lcs_dp(seq1, seq2)
        end = time.time()
        print(f"Result: {result}, Time taken: {end - start:.4f} seconds")

'''
DYNAMIC PROGRAMMING: KNAPSACK PROBLEM

You're in charge of selecting a football (soccer) team from a large pool of players. Each player has a cost and a rating. You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there's no minimum or maximum team size.

General problem statement:
Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.

Input:
1. `weights`: A list of numbers containing weights
2. `profits`: A list of numbers containing profits (same as weights but with different values)
3. `capacity`: The maximum weight the knapsack can hold

Output:
1. `max_profit`: The maximum profit that can be obtained by selecting a subset of the elements weighing no more than capacity.

Test cases:
1. All the elemnents can be included in the knapsack
2. No elements can be included in the knapsack
3. Some elements can be included in the knapsack
4. Multiple combinations of elements can be included in the knapsack
5. Empty weights and profits
6. Only one element can be included in the knapsack
7. Weights and profits are the same
8. Weights and profits are different
9. Capacity is zero
10. Weights and profits have different lengths (invalid input)
11. You do not use the complete capacity 

Recursion approach
1. We'll write a recursive function that computes max_profit(weights[idx:]), profits[idx:], capacity , with idx starting from 0.

2. If weghts[idx] > capacity, the current element cannot be selected, so the maximum profit is the same as max_profit(weights[idx+1:], profits[idx+1:], capacity).

3. Otherwise, there are two possibilities: we either pick weights[idx] or don't. We can recursively compute the maximum.

A. If we don't pick weights[idx], once again the maximum profit for this case is max_profit(weights[idx+1:], profits[idx+1:], capacity)

B. If we pick weights[idx], the maximum profit for this is profits[idx] + max_profit(weight[idx+1:], profits[idx+1:], capacity - weight[idx])

4. If weights[idx:] is empty, the maximum profit for this case is 0.
'''

# # attempt 1 using recursive approach
def max_profit_recursive(weights, profits, capacity):
    def max_profit_helper(weights, profits, capacity, idx):
        if idx >= len(weights):
            return 0
        if weights[idx] > capacity:
            return max_profit_helper(weights, profits, capacity, idx + 1)
        else:
            return max(max_profit_helper(weights, profits, capacity, idx + 1), profits[idx] + max_profit_helper(weights, profits, capacity - weights[idx], idx + 1))
    if len(weights) != len(profits):
        return "Invalid input"
    return max_profit_helper(weights, profits, capacity, 0)

'''
DYNAMIC PROGRAMMING APPROACH:
1. We can use a 2D array to store the maximum profit for each subproblem, where the rows represent the items and the columns represent the capacities from 0 to the given capacity.
2. We fill the table iteratively, starting from the base cases (capacity 0) and building up to the final solution.
3. The time complexity of this approach is O(n*capacity) and the space complexity is O(n*capacity).

'''
# Dynamic programming approach
# def max_profit_dp(weights, profits, capacity):
#     if len(weights) != len(profits):
#         return "Invalid input"
#     n = len(weights)
#     # Create a 2D array to store the maximum profit for each subproblem
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

#     # Fill the table iteratively
#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(dp[i - 1][w], profits[i - 1] + dp[i - 1][w - weights[i - 1]])
#             else:
#                 dp[i][w] = dp[i - 1][w]

#     return dp[n][capacity]

# Memorization approach
def max_profit_memo(weghts, profits, capacity):
    memo = {}
    def helper(weights, profits, capacity, idx):
        if idx >= len(weights):
            return 0
        if (idx, capacity) in memo:
            return memo[(idx, capacity)]
        if weights[idx] > capacity:
            memo[(idx, capacity)] = helper(weights, profits, capacity, idx + 1)
        else:
            memo[(idx, capacity)] = max(helper(weights, profits, capacity, idx + 1), profits[idx] + helper(weights, profits, capacity - weights[idx], idx + 1))
        return memo[(idx, capacity)]
    if len(weights) != len(profits):
        return "Invalid input"
    return helper(weights, profits, capacity, 0)


test0 = {
    'input' : {
        'capacity': 10,
        'weights': [1, 2, 3],   
        'profits': [10, 15, 40]
    },
    'output' : 65
}

test1 = {
    'input' : {
        'capacity': 5,
        'weights': [6, 7, 8],   
        'profits': [10, 15, 40]
    },
    'output' : 0
}

test2 = {
    'input' : {
        'capacity': 6,
        'weights': [1, 2, 3],   
        'profits': [10, 15, 40]
    },
    'output' : 65
}

test3 = {
    'input' : {
        'capacity': 5,
        'weights': [1, 2, 3],   
        'profits': [10, 15, 40]
    },
    'output' : 55
}

test4 = {
    'input' : {
        'capacity': 5,
        'weights': [],   
        'profits': []
    },
    'output' : 0
}

test5 = {
    'input' : {
        'capacity': 5,
        'weights': [1],   
        'profits': [10]
    },
    'output' : 10
}

test6 = {
    'input' : {
        'capacity': 5,
        'weights': [1, 2, 3],   
        'profits': [1, 2, 3]
    },
    'output' : 5
}

test7 = {
    'input' : {
        'capacity': 5,
        'weights': [1, 2, 3],   
        'profits': [10, 20, 30]
    },
    'output' : 50
}

test8 = {
    'input' : {
        'capacity': 0,
        'weights': [1, 2, 3],   
        'profits': [10, 20, 30]
    },
    'output' : 0
}

test9 = {
    'input' : {
        'capacity': 5,
        'weights': [1, 2],   
        'profits': [10]
    },
    'output' : "Invalid input"
}

test10 = {
    'input' : {
        'capacity': 5,
        'weights': [1, 2, 3],   
        'profits': [10, 20]
    },
    'output' : "Invalid input"
}

tests = [ test0, test1, test2, test3, test4, test5, test6, test7, test8, test9, test10 ]

if __name__=="__main__":
    passed = 0
    failed = 0
    total = len(tests)
    for t in tests:
        weights = t['input']['weights']
        profits = t['input']['profits']
        capacity = t['input']['capacity']
        expected_output = t['output']
        result = max_profit_memo(weights, profits, capacity)
        if result == expected_output:
            passed += 1
        elif result != expected_output:
            failed += 1
        else:
            print(f"FAILED: Input: weights={weights}, profits={profits}, capacity={capacity}")
            print(f"Expected: {expected_output}, Actual: {result}")
    print(f"Passed: {passed}/{total}")
    print(f"failed: {failed}/{total}")
    if passed == total:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")
    
