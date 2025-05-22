# a function that removes duplicates from a list while preserving order.
def output_list(inputl):
    output = []
    for i in inputl:
        if i not in output:
            output.append(i)
    return output

num =  int(input("Enter the number of elements you want to add in list:\n"))
input_list = []

for i in range(num):
    input_ele = float(input(f"Enter the element at {i+1} index: "))
    input_list.append(input_ele)

print(f"The original list is:\n{input_list}")
print(f"List after removing duplicates:\n{output_list(input_list)}")
