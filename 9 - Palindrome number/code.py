# LeetCode Problem: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Tags: Math
# Approach: inline check if the number is the same as its reverse by converting it to string and by using slicing.

class Solution(object):
    def isPalindrome(self, x):
            return str(x) == str(x)[::-1]
