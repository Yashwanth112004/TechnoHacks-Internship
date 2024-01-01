def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':    
    result = addition(num1, num2)
    print("Number 1 + Number 2= ", result)
elif choice == '2':
    result = subtraction(num1, num2)
    print("Number 1 - Number 2= ",result)
elif choice == '3':
    result = multiplication(num1, num2)
    print("Number 1 * Number 2= ",result)
elif choice == '4':
    result = division(num1, num2)
    print("Number 1 / Number 2= ",result)
else:
    print("Invalid Input") 
    