# Find second largest element

def second_largest(a):
    largest = float("-inf")
    second_largest = float("-inf")

    for i in a:
        if i > largest:
            second_largest = largest
            largest = i
        elif i >second_largest and i!= largest:
            second_largest = i

    return second_largest


arr = [12, -5, 0, 7, 33, 21, -14, 8, 99, 3]

print(f"Array is as follows:\n{arr}")
print(f"Second Largest element: {second_largest(arr)}")