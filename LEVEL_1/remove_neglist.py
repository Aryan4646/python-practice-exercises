# Remove all negative numbers
num = int(input("Enter the number of elements you want to add in list: "))
input_list = []

for i in range(num):
    element = float(input(f"Enter the element {i+1} in the list: "))
    input_list += [element]

# # Using Loop
# output_list = []
# for z in input_list:
#     if z >= 0:
#         output_list += [z]
# print(f"Input list:\n{input_list}")
# print(f"Output List is:\n{output_list}")

# Using List comprehension
output_list = [x for x in input_list if x >= 0]
print(f"Input list:\n{input_list}")
print(f"Output List is:\n{output_list}")