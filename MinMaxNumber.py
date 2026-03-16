def find(arr):
    min = arr[0]
    max = arr[0]
    for n in arr[1:]:
        if n < min:
            min = n
        elif n > max:
            max = n
    return max,min
arr = list(map(int,input("Enter The Array: ").split()))
max,min = find(arr)
print(f"Maximum Number is :{max}\nMinimum Number is: {min}")
