# Reverse an array

def rev(a):
    new_arr = []
    for i in range(len(a)-1,-1,-1):
        new_arr.append(a[i])
    return new_arr

arr = [12, -5, 0, 7, 33, 21, -14, 8, 99, 3]

print(f"Array is as follows:\n{arr}")
print(f"Reversed array is as follows:\n{rev(arr)}")