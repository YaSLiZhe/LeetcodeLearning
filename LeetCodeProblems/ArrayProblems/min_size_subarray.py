class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum, minL = 0, float("inf")
        p1, p2 = 0, 0
        n = len(nums)
        for p1 in range(n):
            sum += nums[p1]
            while sum >= target:
                minL = min(minL, p1 - p2 + 1)
                sum -= nums[p2]
                p2 += 1
        if minL == float("inf"):
            return 0
        return minL
