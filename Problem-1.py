class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def operate(self, operation: str):
        operation = operation.lower()
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Invalid operation. Choose from: add, subtract, multiply, divide."

if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        operation = input("Enter operation (add, subtract, multiply, divide): ")

        calc = Calculator(a, b)
        result = calc.operate(operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values for a and b.")
