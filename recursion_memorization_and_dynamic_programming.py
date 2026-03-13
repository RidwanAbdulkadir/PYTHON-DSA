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