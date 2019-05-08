# This was asked in Google
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
# Best Solution can be found in LeetCode, Need to check the solution with Binary Search

def twoSum(nums, k):  # O(n^2)
    for i in nums:
        find_val = abs(k-i)
        print (i, find_val)
        if find_val in nums:
            return True
    
    return False

def binary_search(arr, start, end, key):
    mid = (start+end)//2
    
    if start <= end:
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_search(arr, start, mid-1, key)
        else:
            return binary_search(arr, mid+1, end, key)
    else:
        return -1
        
def twoSum(nums, target):
    for idx, i in enumerate(nums):
        find_val = abs(target - i)
        find_val_idx = binary_search(nums, idx+1, len(nums)-1, find_val)
        print(find_val, find_val_idx)
        if find_val_idx != -1:
            return [idx, find_val_idx]

nums = [0, 15, 3, 0]
k = 0
print(twoSum(nums, k))
