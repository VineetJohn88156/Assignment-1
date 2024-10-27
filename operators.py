def arithmetic_operations(a, b):
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b if b != 0 else 'Division by zero error'}")
    print(f"Modulus: {a % b if b != 0 else 'Division by zero error'}")
    print(f"Exponentiation: {a ** b}")

# Example usage
arithmetic_operations(10, 5)
