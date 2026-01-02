def calculator():
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        op = input("Operation (+, -, *, /): ")
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = a / b
        else:
            result = "Invalid operation"
        
        print(f"Result: {result}")
    
    except ValueError:
        print("Enter numbers only")

if __name__ == "__main__":
    calculator()
