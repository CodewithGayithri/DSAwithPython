n = int(input("Enter the Number: "))
num = n
no_of_digits = len(str(num))
total = 0

while num > 0:
    last_digit = num % 10
    total = total + (last_digit ** no_of_digits)
    num = num // 10
print(total == n)
