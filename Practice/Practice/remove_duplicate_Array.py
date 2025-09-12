# Remove duplicates from array

def remove_duplicates(a):
    new_arr = []
    for i in a:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr

arr = [4, 7, 2, 7, 9, 2, 11, 7, 5, 2]

print(f"Array is as follows:\n{arr}")
print(f"New array without duplicates:\n{remove_duplicates(arr)}")