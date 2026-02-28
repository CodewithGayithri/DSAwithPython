def bubblesort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j]> nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums

nums = [6,3,5,7,8]
res = bubblesort(nums) 
print(res)
    
