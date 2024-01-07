def square(nums):
    # arr = []
    # for i in range(len(nums)):
    #     arr.append(nums[i]**2)
    # arr.sort()
    # return arr
    i,j,k = 0,len(nums)-1, len(nums)-1
    res = [float('inf')] * len(nums)
    while i <= j:
        if(nums[i]**2 < nums[j]**2):
            res[k] = nums[j]**2
            j -= 1
        else:
            res[k] = nums[i]**2
            i += 1
        k -= 1
    print(res)
    return res

nums = [-4,-1,0,3,10]
result = square(nums)
print(result)