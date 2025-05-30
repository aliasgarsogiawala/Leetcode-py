# LeetCode Problem: https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Tags: Math
# Approach: Convert the integer to a string, reverse the string, convert the reversed string back to an integer, and check if it is within the 32-bit signed integer range.

class Solution(object):
    def reverse(self, x):
         
        strx=str(x)
        listbox=list(strx)
        listbox.reverse()
        if x<0:
            listbox.remove("-")
            listbox.insert(0,"-")
        revstring = "".join(listbox)
        revnum=int(revstring)
        if revnum < -2147483648 or revnum > 2147483647:
            return 0
        return revnum
        