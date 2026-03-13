# arr= [1,2,3,4,5]
# print(arr[::-1])

arr = [int(i) for i in input("Enter The elements: ").split()]
i = 0
mid = len(arr)//2
while i<mid:
    arr[i] ,arr[len(arr)-i-1] = arr[len(arr)-i-1],arr[i]
    i +=1
print(arr)  