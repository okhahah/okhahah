#program to make a simple calculator

#Function to add to numbers
def add(x, y):
    return x + y

#Function to subtract two numbers
def subtract(x, y):
    return x - y

#Function to multiple two numbers
def multiply(x, y):
    return x * y

#Function to divide two numbers
def divide(x, y):
    return x / y


print("select operation.")
print("1.add")
print("2.subtract")
print("3.multipy")
print("4.divide")

while True:
    choice = input("enter choice(1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        num1 = (input("enter first number: "))
        num2 = (input("Enter second number: "))

        if choice == '1':
            print(num1, '+', num2, "=", add(num1, num2))

        elif choice == '2':
            Print(num1, "-", num2, "=", subtract(num1,num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            break
            
                  


