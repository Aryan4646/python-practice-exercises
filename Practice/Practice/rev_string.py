# Reverse a string

input_Str = input("Enter the string: ")

print(f"Input string: {input_Str}")

# Using slicing
output_string = input_Str[::-1]

# Using loops
# output_string = ""
# for i in range(len(input_Str)-1,-1,-1):
#     output_string += input_Str[i]

print(f"Reversed string: {output_string}")