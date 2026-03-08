# num = int(input("Enter Number: "))
# result = []
# def Factors(num):
#     for i in range(1,num+1):
#         if num % i == 0:
#             result.append(i)
#     return result

# res = Factors(num)
# print(res)


#optimal Solution
result=[]
from math import sqrt
def factors(num):
    for i in range(1,int(sqrt(num))+1):
        if num%i==0:
            result.append(i)
            if num//i!= i:
                result.append(num//i)
    result.sort()
    return result
num = int(input("Enter Number: "))
res = factors(num)
print("Factors Of Given Number: ",res)
