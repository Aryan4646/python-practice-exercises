# Print all pairs in array with given sum

def pairs(a,tar):
    pair_list = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j]== tar:
                pair_list.append((a[i],a[j]))
    return pair_list


arr = [1, 5, 7, -1, 5, 3, 9, 2, 8, 6]
target_sum = 10

print(f"The original array is as follows:\n{arr}")
print(f"The pairs are as follows:\n{pairs(arr,target_sum)}")