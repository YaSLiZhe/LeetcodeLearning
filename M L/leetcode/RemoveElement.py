class Solution(object):
    def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        
        i = 0
        L = len(nums)
        # for i in range(L):
        while i < L:
            if nums[i] == val:
                for j in range(i+1, L):
                    nums[j-1] = nums[j]
                L -= 1
                i -= 1
            i += 1
        return L
        """

#       双指针法（快慢指针法）： 通过一个快指针和慢指针在一个for循环下完成两个for循环的工作。
#       定义快慢指针
#       快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
#       慢指针：指向更新 新数组下标的位置

        slowIndex, fastIndex = 0, 0
        L = len(nums)
        # 等于val时，fastindex++，slowindex不加；
        # 不等于时，一起++
        for fastIndex in range(0,L):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex
    
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2
    nums = [3,2,2,3]
    val = 3
    result = removeElement(nums, val)
    print(result)