FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

while True:
    temperature = input("Enter the temperature to convert: ")
    if not temperature.replace('.','',1).isdigit():
        print("Invalid temperature input. Please enter a numeric value.")
        continue  # Loop back to asking for the temperature again
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (F/C): ").strip().upper()
    
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius:.2f}°C")
        break  # Exit the loop after successful conversion
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit:.2f}°F")
        break  # Exit the loop after successful conversion
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
