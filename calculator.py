# Simple Calculator Script in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    # Take user input for the operation
    choice = input("Enter the operation number (1/2/3/4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid input. Please try again.")
        return
    
    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    
    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        operation = '/'
    
    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()
    