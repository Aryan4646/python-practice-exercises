# Search for an element (linear search)

def is_element(a,element):
    for i in range(len(a)):
        if a[i] == element:
            return i
    return -1

arr = [3, 7, 2, 9, 5, 11, 6]
target = int(input("Enter the target element: "))
print(f"\nArray is as follows:\n{arr}")
print(f"The target element is : {target}")

is_element_exist = is_element(arr,target)

if is_element_exist == -1:
    print(f"Element {target} is not in array.")
else:
    print(f"Element {target} is at index {is_element_exist}")