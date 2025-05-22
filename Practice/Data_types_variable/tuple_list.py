# Create a program that takes a list of tuples (name, age) and returns a sorted list by age.

def sorted_list(input_list):
    sort = sorted(input_list, key=lambda x:x[1])
    return sort

input_list = []
num = int(input("Enter the number of tuple you would like to add: "))

for i in range(num):
    name_ele = input(f"Enter the name at index {i+1} for tuple: ")
    age_ele = int(input(f"Enter the age at index {i+1} for tuple: "))
    tuples = name_ele,age_ele
    input_list.append(tuples)

print(f"Original list is: {input_list}")

print(f"Sorted list by age: {sorted_list(input_list)}")
