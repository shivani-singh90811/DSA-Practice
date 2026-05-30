# Contains Duplicate - LeetCode #217
# Difficulty: Easy
# Topic: Arrays, Set
# Time: O(n) | Space: O(n)

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums)