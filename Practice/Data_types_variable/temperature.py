# Program to convert temperatures between Celsius, Fahrenheit, and Kelvin.

tempera = int(input("Press 1 to enter temperature in Celsius.\n"
      "Press 2 to enter temperature in Fahrenheit.\n"
      "Press 3 to enter temperature in Kelvin.\n"))
temp = float(input("Enter the temperature: "))
conversion = int(input("Press 1 to convert temperature in Celsius.\n"
                   "Press 2 to convert temperature in Fahrenheit.\n"
                   "Press 3 to convert temperature in Kelvin."))

if tempera == conversion:
      print("No need of conversion temperature is already in the same format.")
elif tempera == 1 and conversion == 2:
      print(f"{temp} celsius in fahrenheit is {((9/5)*temp)+32}")
elif tempera == 1 and conversion == 3:
      print(f"{temp} celsius in kelvin is {temp+273.15}")
elif tempera == 2 and conversion == 1:
      print(f"{temp} fahrenheit in celsius is {(temp-32)*(5/9)}")
elif tempera == 2 and conversion == 3:
      print(f"{temp} fahrenheit in kelvin is {((temp-32)*(5/9))+273.15}")
elif tempera == 3 and conversion == 1:
      print(f"{temp} kelvin in celsius is {temp-273.15}")
elif tempera == 3 and conversion == 2:
      print(f"{temp} kelvin in fahrenheit is {((temp-273.15)*(9/5))+32}")