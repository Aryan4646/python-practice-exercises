# Create dictionary from two lists (zip)
num1 = int(input("Enter the number of elements you want to add in list 1: "))
key = []
value = []
for i in range(num1):
    list_element1 = float(input(f"Enter the {i+1} key of the list 1: "))
    if list_element1 not in key:
        key.append(list_element1)
count = 0
for x in key:
        count += 1
print(f"Number of keys are {key} so you should add {count} values.")
for z in range(count):
    list_element2 = float(input(f"Enter the {z+1} element of the list 2: "))
    value.append(list_element2)
print(f"List 1 is as follows:\n{key}")
print(f"List 2 is as follows:\n{value}")
print(f"Dictionary using zip function is as follows:\n{dict(zip(key,value))}")


