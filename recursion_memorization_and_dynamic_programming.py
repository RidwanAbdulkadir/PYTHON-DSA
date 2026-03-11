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
DYNAMIC PROGRAMMING APPROACH:

1.  
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


