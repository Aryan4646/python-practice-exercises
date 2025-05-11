num = int(input("Enter the number of elements you want to add in list: "))
input_list = []
largest = float("-inf")
second_largest = float("-inf")
for i in range(num):
    list_element = float(input(f"Enter the {i+1} element of the list: "))
    input_list.append(list_element)
for i in input_list:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(f"The list is:\n{input_list}")
print(f"\nThe largest element is: {largest}")
if second_largest == float("-inf"):
    print("There is no distinct second largest element.")
else:
    print(f"The second largest element is: {second_largest}")
