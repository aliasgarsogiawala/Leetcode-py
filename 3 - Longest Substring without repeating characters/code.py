# LeetCode Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Tags: String , Hash Table , Sliding Window
# Approach: Used a sliding window with a list to track non-repeating characters and updated the max length whenever a duplicate was found and the window was adjusted.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        listseen=[]
        max_len=0
        for i in s:
            if i not in listseen:
                listseen.append(i)
            else:
                index=listseen.index(i)
                listseen=listseen[index+1:]
                listseen.append(i)
            max_len=max(max_len,len(listseen))
        return max_len