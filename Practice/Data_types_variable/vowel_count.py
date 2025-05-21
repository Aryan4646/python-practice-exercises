# Implement a function that takes a string input and returns the count of each vowel.
def count_vow(input):
    count = 0
    for i in input.lower():
        if i in "aieou":
            count += 1
    return count

input_str = input("Enter the string: ")
print(f"The number of vowel in string {input_str} is equal to {count_vow(input_str)}.")