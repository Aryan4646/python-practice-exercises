# Find longest word in string

def list_check(l):
    biggest = ""
    for i in l:
        if len(i) > len(biggest):
            biggest = i
    return biggest

def longest_word(s):
    new_l = []
    word = ""
    for i in s:
        if i == " ":
            new_l.append(word)
            word = ""
        else:
            word += i
    new_l.append(word)

    longest = list_check(new_l)
    return longest

s = "The quick brown fox jumps over the lazy hippopotamus"

print(f"The string is as follows:\n{s}")
print(f"The longest word in string is: {longest_word(s)}")


