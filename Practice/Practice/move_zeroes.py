# Move zeros to end of array

def modified_arr(a):
    new_array = []
    for i in a:
        if i != 0:
            new_array.append(i)
    diff = len(a) - len(new_array)
    while diff != 0:
        new_array.append(0)
        diff -= 1
    return new_array

arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6]

print(f"The original array is as follows:\n{arr}")
print(f"The modified array is as follows:\n{modified_arr(arr)}")