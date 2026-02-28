nums = [3,8,4,2,5,1,6,9,7]

def SelectionSort(nums):
    for i in range(0,len(nums)):
        min_ind = i
        for j in range(i+1, len(nums)):
            if(nums[min_ind] < nums[j]): 
                # For Descending Orderif(nums[min_ind] > nums[j]):
                min_ind = j
        nums[i],nums[min_ind] = nums[min_ind], nums[i]
    return nums
res = SelectionSort(nums)
print(res)