num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
for i in range(num):
    list_element = float(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)
largest = float("-inf")
smallest = float("+inf")
total = 0

for x in input_list:
    total += x
    if x >= largest:
        largest = x
    if x <= smallest:
        smallest = x

print(f"The input list is:\n{input_list}")
print(f"The maximum element in the list is: {largest}")
print(f"The minimum element in the list is: {smallest}")
print(f"The average of elements of list: {total/num}")



