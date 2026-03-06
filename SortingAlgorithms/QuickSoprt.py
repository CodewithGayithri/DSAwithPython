def partition(nums, low, high):
    pivot = nums[low]
    i=low, j=high
    while i<j:
        while nums[i]< pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j <=low + 1:
            j -= 1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return i
nums = list(int,input("enter The Array: "))
def quicksort(nums,low,high):
    if i<j:
        p_indx = partition(nums,low,high)
        quicksort(nums,low,p_indx-1)
        quicksort(nums,p_indx+1, high)

