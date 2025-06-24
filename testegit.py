def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."
    else:
        return "Invalid operation."


# Example usage:
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (add, subtract, multiply, divide): ")
    result = calculate(a, b, op)
    print("Result:", result)
