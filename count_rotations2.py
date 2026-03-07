'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.
'''

# def count_rotations(nums):
#     left, right = 0, len(nums) - 1
    
#     while left < right:
#         mid = (left + right) // 2
        
#         # Check if mid element is greater than the rightmost element
#         if nums[mid] > nums[right]:
#             # The rotation point is to the right of mid
#             left = mid + 1
#         else:
#             # The rotation point is at mid or to the left of mid
#             right = mid
            
#     return left  # or right, since left == right


# #linear search approach
# def count_rotations(nums):
#     position = 0               # Initial value of position
    
#     while True:                     # Loop until we find the rotation point
        
#         # Success criteria: check whether the number at the current position is smaller than the one before it
#         if position > 0 and nums[position] < nums[position - 1]:   # Perform the check
#             return position
        
#         # Move to the next position
#         position += 1
        
#         # If we have checked all positions and found no rotation point, return 0
#         if position >= len(nums):
#             return 0

# nums = [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
# result = count_rotations(nums)
# # print(result)


'''
Here's a slightly advanced extension to this problem:

You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a target number. Write a function to find the position of the target number within the rotated list. You can assume that all the numbers in the list are unique.

'''

#we need to solve this problem using binary searCH
# Function to find the position of a target number in a rotated sorted list
def find_target_in_rotated(nums, target):
    """
    Find the position of a target number in a rotated sorted list.
    Time Complexity: O(log N)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid 
        
        # Determine which side is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            # Check if target is in the sorted left side
            if nums[left] <= target < nums[mid]:
                right = mid - 1  # Search left
            else:
                left = mid + 1   # Search right
        else:  # Right side is sorted
            # Check if target is in the sorted right side
            if nums[mid] < target <= nums[right]:
                left = mid + 1   # Search right
            else:
                right = mid - 1  # Search left
    
    return -1  # Target not found
 

# Test the functions
nums = [5, 6, 9, 0, 2, 3, 4]
target = 9

position = find_target_in_rotated(nums, target)

if position != -1:
    print(f"The target number {target} occurs at position {position}.")
else:
    print(f"Target number {target} not found in the list.")