# Two Sum — LeetCode #1
# Difficulty: Easy
# Topic: Arrays, HashMap

# Problem:
# Given array nums and target
# Return indices of two numbers
# that add up to target

# Approach: HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Test
print(twoSum([2,7,11,15], 9))   # [0,1]
print(twoSum([3,2,4], 6))       # [1,2]