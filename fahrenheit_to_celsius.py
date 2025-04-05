# Function to convert Fahrenheit to Celsius
def convert(fahrenheit):
   # Convert Fahrenheit to Celsius
    celsius = 5/9 * (fahrenheit - 32)
    return celsius

def main():
    fahrenheit_temp = eval(input("Enter temperature in Fahrenheit: ")) # Accept temperature input from the user in Fahrenheit
    celsius = convert(fahrenheit)
    print(f"The temperature in Celsius is: {celsius:.2f}")
    
    # Check if it's hot or cold
    if celsius > 20:
        print("IT'S HOT HERE")
    else:
        print("IT'S COLD HERE")
main()
