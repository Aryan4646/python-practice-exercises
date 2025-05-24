"""Create a function that opens a file and reads integers line by line,
 handling invalid data with custom exceptions."""

class Integerexception(Exception):
    pass

def fileopener(t):
    try:
        file = open(t,'r')
        c = file.readlines()
        for i in c:
            try:
                p = int(i)
                print(p)
            except ValueError:
                raise Integerexception(f"Invalid data format string")
        file.close()
    except FileNotFoundError:
        print("File not found")
fileopener("txt")