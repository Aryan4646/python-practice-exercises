# Remove vowels from the string
input_string = input("Enter the string: ")
print(f"\nOriginal string is: {input_string}")
output_string = ""

for i in input_string:
    if i.casefold() not in "aeiou":
        output_string += i
print(f"Modified string: {output_string}")