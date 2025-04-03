def convert(fahrenheit_temp):
    celsius = 5/9 * (fahrenheit_temp - 32)
    return celsius

def main():
    fahrenheit_temp = eval(input("Enter temperature in Fahrenheit: "))
    celsius = convert(fahrenheit_temp)
    print(f"The temperature in Celsius is: {celsius:.2f}")
    
    if celsius > 20:
        print("IT'S HOT HERE")
    else:
        print("IT'S COLD HERE")
main()