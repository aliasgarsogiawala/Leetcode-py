import collections

class FindSumPairs(object):
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counter = collections.Counter(nums2)

    def add(self, index, val):
        old = self.nums2[index]
        new = old + val
        self.counter[old] -= 1
        if self.counter[old] == 0:
            del self.counter[old]
        self.nums2[index] = new
        self.counter[new] += 1

    def count(self, tot):
        ans = 0
        for num in self.nums1:
            complement = tot - num
            ans += self.counter.get(complement, 0)
        return ans
