# Count frequency of an element

num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
count = 0
for i in range(num):
    list_element = float(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)
element = float(input("\nEnter the element whose frequency you want to calculate: "))

for z in input_list:
    if element == z:
        count += 1
print(f"\nOriginal List is:\n{input_list}")
if count > 0:
    print(f"Frequency of element {element}: {count}")
else:
    print(f"No element found.")
