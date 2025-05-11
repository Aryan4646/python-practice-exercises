# Remove duplicates from list
num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
output_list = []
for i in range(num):
    list_element = float(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)
for i in input_list:
    if i not in output_list:
        output_list.append(i)
print(f"\nList is :\n{input_list}")
print(f"List after removing duplicates:\n{output_list}")