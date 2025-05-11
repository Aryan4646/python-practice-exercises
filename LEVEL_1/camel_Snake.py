# Convert camelCase to snake_case

input_string = input("Enter the string: ")
print(f"\nEnter the camelCase string : {input_string}")
output_string = ""

for i in input_string:
    if i.isupper():
        output_string += "_"
        output_string += i.lower()
    else:
        output_string += i
print(f"snake_case string is: {output_string}")