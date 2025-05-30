# LeetCode Problem: https://leetcode.com/problems/two-sum
# Difficulty: Easy
# Tags: Array , Hash Table
# Approach: Check if the complement of the current number is in the dictionary, if not add the current number to the dictionary with its index as the value.
# If the complement is in the dictionary, return the index of the complement and the current index.


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
