class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p2 = 0
        n = len(nums)
        for p1 in range(n):
            if nums[p1] != val:
                nums[p2] = nums[p1]
                p2 += 1
        return p2
