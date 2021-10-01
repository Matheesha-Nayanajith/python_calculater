# Program make a simple calculator

#  adds two numbers
def add(x, y):
    return x + y

#  subtracts two numbers
def subtract(x, y):
    return x - y

#  multiplies two numbers
def multiply(x, y):
    return x * y

#  divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

op = input()

print("1st Number")
num1 = int(input())
print("2nd Number")
num2 = int(input())

if op == '1':
    print(add(num1,num2))
elif op == '2':
    print(subtract(num1, num2))
elif op == '3':
    print(multiply(num1, num2))
elif op == '4':
    print(divide(num1, num2))
else:
    print('Invalid input')


