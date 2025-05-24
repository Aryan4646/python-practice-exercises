"""Write code that tries to convert a list of strings to integers
and catches/converts errors accordingly."""

sample_list = ["42", "100", "abc", "3.14", "-7", "hello", "0", "999", "12three", "75"]
new_list = []
error_Raised = []

for i in sample_list:
    try:
        p = int(i)
    except ValueError:
        error_Raised.append(i)
        print(f"This {i} can not be converted to integer. Error")
    else:
        new_list.append(p)
print(f"Sample list: {sample_list}")
print(f"New list of integer: {new_list}")
print(f"Error raised at: {error_Raised}")

