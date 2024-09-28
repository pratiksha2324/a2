#Program to swap two variables

def swap(num1, num2):
    num1, num2 = num2, num1
    return num1, num2


num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
print("Before swapping: ")
print("num1 = ", num1)
print("num2 = ", num2)

num1, num2 = swap(num1, num2)
print("After swapping: ")
print("num1 = ", num1)
print("num2 = ", num2)