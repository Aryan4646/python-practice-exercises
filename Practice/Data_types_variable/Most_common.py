# Implement a program that finds the most common element in a list.

def common(l):
    dictionary = {}
    for i in l:
        if i in dictionary:
            dictionary[i] = dictionary.get(i)+1
        else:
            dictionary[i] = 1
    key = None
    freq = 0
    for i in dictionary:
        if freq < dictionary[i]:
            freq = dictionary[i]
            key = i
    return key, freq


input_list = []
num = int(input("Enter the number of elements you would like to add: "))

for i in range(num):
    input_ele = input(f"Enter the element at index {i+1}: ")
    input_list.append(input_ele)

print(f"Original list is: {input_list}")
key, freq = common(input_list)
if key == None:
    print("All elements have same occurence")
else:
    print(f"The most common element in the list is {key} with frequency of:{freq}")
