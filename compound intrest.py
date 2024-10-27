def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal
    print(f"Compound Interest: {interest}")
    print(f"Total Amount: {amount}")

# Example
compound_interest(1000, 5, 2)