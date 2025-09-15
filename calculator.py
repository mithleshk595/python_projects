def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def substract(x, y):
    return x - y

def division(x ,y):
    if y != 0:
        return x / y
    else:

        return "Error! division by Zero"
    
print("select operation:")
print("1 Add :")
print("2 multiply:")
print("3 substract:")
print("4 division:")

choice = input("Enter choice(1/2/3/4):")

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice == "1":
    print("result =", add(num1, num2))
elif choice == "2":
    print("result= ", multiply(num1, num2))
elif choice == "3":
    print("result= ", substract(num1, num2))
elif choice == "4":
    print("result= ", division(num1, num2))

else:
    print("invalid user")



def Add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y !=0:
        return x / y
    else:
        return "Error! divide by divide "
    
print("selection operation:")
print("1 Add:")
print("2 substract:")
print("3 multiply:")
print("4 divide:")



choice = input("Enter choice (1/2/3/4):")

num1 = float("Enter first number :")
num2 = float("Enter second n umber :")

if choice == "1":
    print("result =", Add(num1, num2))

elif choice == "2":    
    print("result =", substract(num1, num2))

elif choice == "3":
    print("result =", multiply(num1, num2))
elif choice == "4":

    print("result =", divide(num1, num2))

else:
    print("invalid user")



    