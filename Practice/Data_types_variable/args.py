# Create a function that accepts arbitrary numbers of arguments and returns their average.

def avg(*args):
    if not args:
        return 0
    return sum(args) / len(args)

num = int(input("Enter the number of elements in list: "))
input_l = []

for i in range(num):
    element = float(input(f"Enter the element at {i+1} index: "))
    input_l.append(element)

print(f"The input list is: {input_l}")
print(f"The average of elements is:{avg(*input_l)}")