# Rotate array by k position

def rotate_array(a,k):
    n = len(a)
    k %= n
    # Slicing way
    # new_Array = a[n-k:n]+a[0:n-k]

    # Another approach
    new_Array= []
    for i in range(n-k,n):
        new_Array.append(a[i])
    for j in range(0,n-k):
        new_Array.append(a[j])
    return new_Array

arr = [3, 7, 2, 9, 5, 11, 6]
position = int(input("Enter by how many position you want to rotate the array: "))

print(f"Array is as follows:\n{arr}")
print(f"You want to rotate array by {position}.")
print(f"New array is as follows: {rotate_array(arr,position)}")