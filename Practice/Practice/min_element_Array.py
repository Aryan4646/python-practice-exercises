# Minimum element of array

def min_Array(a):
    min_element = float('inf')
    for i in a:
        if i < min_element:
            min_element = i
    return min_element

arr = [12, -5, 0, 7, 33, 21, -14, 8, 99, 3]

print(f"Array is as follows:\n{arr}")
print(f"The minimum element of array: {min_Array(arr)}")