num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
total = 0
for i in range(num):
    list_element = float(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)

for z in input_list:
    total += z
print(f"The input list is:\n{input_list}")
print(f"The sum of element of list:{total}")