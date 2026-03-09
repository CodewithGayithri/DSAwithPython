stack = []

def push():
    user = int(input("Enter the elemnt: "))
    stack.append(user)

def pop():
    if len(stack) == -1:
        print("Empty Stack")
    else:
        e = stack.pop()
        print("Deleted Item: ",e)

def access():
    return stack


while True:
    print("Choose the Operation\n1.Append \n2.pop\n3.access\n4.Exit")
    choose =int(input())
    if choose == 1:
        push()
    elif choose == 2:
        pop()
    elif choose == 3:
        access()
        print(stack)
    elif choose == 4:
        break
    else:
        print("Please Choose Valid Option: ") 
        continue
    