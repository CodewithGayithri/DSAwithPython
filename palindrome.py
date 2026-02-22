n = int(input("Enter Number: "))
num = n
res = 0

while num > 0:
    last_digit = num % 10
    res = (res * 10) + last_digit
    num = num // 10
print(n == res)
