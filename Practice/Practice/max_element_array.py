# Find maximum element in array

def max_Array(a):
    max_element = float('-inf')
    for i in a:
        if i > max_element:
            max_element = i
    return max_element

arr = [12, -5, 0, 7, 33, 21, -14, 8, 99, 3]

print(f"Array is as follows:\n{arr}")
print(f"The maximum element of array: {max_Array(arr)}")