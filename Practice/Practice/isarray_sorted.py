# Check if array is sorted

def is_sorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

# arr = [3, 7, 2, 9, 5, 11, 6]
arr = [7, 7, 7, 7, 7]
# Expected: Sorted (non-decreasing)



check = is_sorted(arr)

print(f"Array is as follows:\n{arr}")
if check:
    print("Yes array is sorted")
else:
    print("No array is not sorted")