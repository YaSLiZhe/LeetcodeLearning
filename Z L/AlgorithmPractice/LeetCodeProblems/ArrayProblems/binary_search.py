class Solution:
    def search(self, nums, target) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = l + (r - l)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
# https://leetcode.com/problems/binary-search/
