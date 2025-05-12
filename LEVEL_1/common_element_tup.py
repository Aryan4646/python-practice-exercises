num1 = int(input("Enter how many element you want in tuple 1:"))
input_list_1 = []
input_list_2 = []
for i in range(num1):
    element = input(f"Enter the element {i+1} in the tuple 1: ")
    input_list_1.append(element)
num2 = int(input("Enter how many element you want in tuple 2:"))
for i in range(num2):
    element = input(f"Enter the element {i+1} in the tuple 2: ")
    input_list_2.append(element)

result_tuple_1 = tuple(input_list_1)
result_tuple_2 = tuple(input_list_2)
common = []
for i in result_tuple_1:
    if i in set(result_tuple_2):
            common.append(i)
print(f"Tuple 1:\n{result_tuple_1}")
print(f"Tuple 2:\n{result_tuple_2}")
if len(common) > 0:
    print(f"Common element in tuple 1 and tuple 2 : {tuple(common)}")
else:
    print("None elements common")