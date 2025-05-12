# List of squares (loop + list comprehension)

# # Using loops
# num = int(input("Enter upto which number you want to create a list: "))
# output_list =[]
# for i in range(1, num+1):
#     output_list.append(i**2)
# print(f"List of squares:\n{output_list}")

# Using List_Comprehension
num = int(input("Enter upto which number you want to create a list: "))
output_list = [x**2 for x in range(1, num+1)]

print(f"List of squares:\n{output_list}")