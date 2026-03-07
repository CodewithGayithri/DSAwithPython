num = int(input("Enter Number: "))
result = []
def Factors(num):
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    return result

res = Factors(num)
print(res)