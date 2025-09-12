# Sum of all elements in array

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

arr = [3, 7, 2, 9, 5, 11, 6]

print(f"Array is as follows:\n{arr}")
print(f"Sum of the elements of this array: {array_sum(arr)}")