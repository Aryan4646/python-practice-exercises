# Create a tuple from user input

num = int(input("Enter how many element you want in tuple:"))
input_list = []

for i in range(num):
    element = input(f"Enter the element {i+1} in the tuple: ")
    input_list.append(element)

result_tuple = tuple(input_list)

print(f"The tuple is:\n{result_tuple}")