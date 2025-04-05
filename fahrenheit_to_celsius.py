def convert(fahrenheit):
    return 5/9 * (fahrenheit - 32)

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = convert(fahrenheit)
print(f"Temperature in Celsius: {celsius:.2f}")
print("IT'S HOT HERE" if celsius > 20 else "IT'S COLD HERE")
