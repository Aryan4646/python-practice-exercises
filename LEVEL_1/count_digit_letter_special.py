strr = input("Enter the string: ")
count_dig = 0
count_letter = 0
count_special = 0
print(f"\nString is:{strr}")
for i in strr:
    if i.isalnum():
        if i.isalpha():
            count_letter += 1
        else:
            count_dig += 1
    else:
        count_special += 1
print(f"\nThe number of digits in {strr} is : {count_dig}")
print(f"The number of letters in {strr} is : {count_letter}")
print(f"The number of special characters in {strr} is : {count_special}")