# Separate even and odd numbers
num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
even_list =[]
odd_list =[]
for i in range(num):
    list_element = int(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)
for z in input_list:
    if z%2 == 0:
        even_list.append(z)
    else:
        odd_list.append(z)
print(f"Original List is:\n{input_list}")
print(f"Even List is :\n{even_list}")
print(f"Odd List is:\n{odd_list}")