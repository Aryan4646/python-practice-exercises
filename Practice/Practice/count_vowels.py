# Count vowels in a string

def vowels(s):
    vowel = "aeiouAIEOU"
    count = 0
    for i in s:
        if i in vowel:
            count +=1
    return count

input_string = input("Enter the string: ")

print(f"Input string: {input_string}")
print(f"The number of vowels in string: {vowels(input_string)}")