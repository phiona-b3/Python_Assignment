def convert(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)

fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
celsius_temp = convert(fahrenheit_temp)

print(f"Celsius: {celsius_temp:.2f}")

if celsius_temp > 20:
    print("IT'S HOT HERE")
else:
    print("IT’S COLD HERE")



