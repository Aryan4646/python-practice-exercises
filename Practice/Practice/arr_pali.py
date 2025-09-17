# Check if array is palindrome

def palindrome_Arr(a):
    a_new = a[-1::-1]
    for i in range(len(a)):
        if a[i] != a_new[i]:
            return False
    return True

arr= [1, 2, 3, 2, 1]

print(f"The original array is as follows:\n{arr}")
is_pali = palindrome_Arr(arr)

if is_pali:
    print("Yes, The array is palindrome.")
else:
    print("No, The array is not palindrome.")