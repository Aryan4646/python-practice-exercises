# Find missing number in 1..N

# 1st approach

# def max_Array(a):
#     max_element = float('-inf')
#     for i in a:
#         if i > max_element:
#             max_element = i
#     return max_element
#
# def missing(a):
#     max_element = max_Array(a)
#     for i in range(1,max_element+1):
#         if i in a:
#             pass
#         else:
#             return i
#     return "Not Found"

# 2nd approach

def max_Array(a):
    max_element = float('-inf')
    for i in a:
        if i > max_element:
            max_element = i
    return max_element

def missing(a):
    max_element = max_Array(a)
    total_sum = (max_element*(max_element+1))/2
    arr_sum = 0
    for i in a:
        arr_sum+=i
    if total_sum-arr_sum == 0:
        return "Not found"
    else:
        return total_sum-arr_sum

arr = [1, 2, 4, 6, 3, 7, 8, 10, 9]

print(f"The original array is as follows:\n{arr}")

is_missing = missing(arr)

if is_missing == "Not Found":
    print(f"There is no missing element.")
else:
    print(f"The missing element is:{is_missing}")