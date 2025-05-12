num = int(input("Enter how many element you want in tuple:"))
input_list = []

for i in range(num):
    element = input(f"Enter the element {i+1} in the tuple: ")
    input_list.append(element)

result_tuple = tuple(input_list)

search_element = input("Enter the element you want to find: ")

if search_element in result_tuple:
    print(f"Yes {search_element} is present in tuple\n{result_tuple}")
else:
    print(f"No {search_element} is not present in tuple\n{result_tuple}")