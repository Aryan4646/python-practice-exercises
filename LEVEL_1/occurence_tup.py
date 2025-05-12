num = int(input("Enter how many element you want in tuple:"))
input_list = []
count = 0
for i in range(num):
    element = input(f"Enter the element {i+1} in the tuple: ")
    input_list.append(element)

result_tuple = tuple(input_list)

search_element = input("Enter the element you want to find occurence : ")

for z in result_tuple:
    if search_element == z:
        count += 1
if count:
    print(f"Yes {search_element} is present in tuple\n{result_tuple} with {count} occurence")
else:
    print(f"No {search_element} is not present in tuple\n{result_tuple} so {count} occurence")