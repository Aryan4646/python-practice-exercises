# Count words in a string

def words_number(s):
    new_l = []
    word = ""
    for i in s:
        if i == " ":
            new_l.append(word)
            word = ""
        else:
            word += i
    new_l.append(word)

    return len(new_l)

s = "The quick brown fox jumps over the lazy hippopotamus"

print(f"The string is as follows:\n{s}")
print(f"The number of words in string: {words_number(s)}")