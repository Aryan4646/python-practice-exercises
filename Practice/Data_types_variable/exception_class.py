# Define your own exception class and use it in a function to validate input data.

class InputDataError(Exception):
    pass

def func(l):
    new_l = []
    for i in l:
        try:
            try:
                p = int(i)
                new_l.append(p)
            except ValueError:
                raise InputDataError(f"'{i}' is not a valid integer.")
        except InputDataError as e:
            print(f"Input data error: {e}")
    return new_l

input_l = [1, "ab", 43 ,3.6, 0 , 'j',3 , 2]
output_l = func(input_l)

print(f"Input List is: {input_l}")
print(f"Output List is: {output_l}")