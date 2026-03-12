# user = input("Enter String: ")
# n = len(user)
# left = 0
# right = n - 1
# def func(user,left,right):
#     while left < right:
#         if user[left] != user[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(func(user,left,right))

#Using Recursion
str = input("Enter String: ")
n = len(str)
left = 0
right = n-1

def is_str_palindrome(str,left,right):
    while left < right:
        if str[left] != str[right]:
            return False
        return is_str_palindrome(str,left+1,right-1)
    return True
print(is_str_palindrome(str,left,right))
    
