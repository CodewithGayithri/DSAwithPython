def find(arr):
    min = arr[0]
    max = arr[0]
    for n in arr[1:]:
        if n < min:
            min = n
        elif n > max:
            max = n
    return max
arr = [2,4,10,6,7]
res = find(arr)
print(res)