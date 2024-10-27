def temperature_conversion():
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * (5/9)
    print(f"Temperature in Celsius: {c}")

    c = float(input("Enter temperature in Celsius: "))
    f = (c * (9/5)) + 32
    print(f"Temperature in Fahrenheit: {f}")

temperature_conversion()