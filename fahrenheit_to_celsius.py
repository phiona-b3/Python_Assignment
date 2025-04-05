# Function to convert Fahrenheit to Celsius
def convert(fahrenheit):
    # Convert Fahrenheit to Celsius
    celsius = 5/9 * (fahrenheit - 32)
    return celsius

# Accept temperature input from the user in Fahrenheit
fahrenheit = eval(input("Enter temperature in Fahrenheit: "))

celsius = convert(fahrenheit)

# Print the Celsius value
print(f"Temperature in Celsius: {celsius:.2f}")

# Check if it's hot or cold
if celsius > 20:
    print("ITS HOT HERE")
else:
    print("ITS COLD HERE")


