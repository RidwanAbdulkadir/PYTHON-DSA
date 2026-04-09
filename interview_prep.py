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

'''

def find_subarray_with_sum(arr, target_sum):
    current_sum = 0
    start_index = 0

    for end_index in range(len(arr)):
        current_sum += arr[end_index]

        while current_sum > target_sum and start_index <= end_index:
            current_sum -= arr[start_index]
            start_index += 1

        if current_sum == target_sum:
            return f"Subarray found from index {start_index} to {end_index}"

    return "No subarray found"  

# Test cases
arr1 = [1, 2, 3, 7, 5]
sum1 = 12
print(find_subarray_with_sum(arr1, sum1))  # Output: Subarray found from index 2 to 4

arr2 = [1, 2, 3, 4, 5]
sum2 = 9
print(find_subarray_with_sum(arr2, sum2))  # Output: Subarray found from index 1 to 3

arr3 = [1, 2, 3, 4, 5]
sum3 = 15
print(find_subarray_with_sum(arr3, sum3))  # Output: Subarray found from index 0 to 4

arr4 = [1, 2, 3, 4, 5]
sum4 = 20
print(find_subarray_with_sum(arr4, sum4))  # Output: No subarray found