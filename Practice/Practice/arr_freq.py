# Count frequency of each element in array

def freq_arr(arr):
    freq_dict = {}
    for i in arr:
        freq_dict[i] = freq_dict.get(i,0) +1
    return freq_dict

arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6]

print(f"The original array is as follows:\n{arr}")
print(f"The frequnecy of each element is as follows:\n{freq_arr(arr)}")