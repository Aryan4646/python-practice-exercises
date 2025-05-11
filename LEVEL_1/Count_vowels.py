# Count Vowels in a string
strr = input("Enter the string: ")
print(f"\nString is:{strr}")
count_vow = 0
count_conso = 0
strr = strr.casefold()
for i in strr:
    if i.isalpha():
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count_vow += 1
        else:
            count_conso += 1
print(f"The number of vowels in string ({strr}) is : {count_vow}")
print(f"The number of consonants in string ({strr}) is : {count_conso}")







