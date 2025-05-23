# Implement a decorator that logs the arguments and return value of any function.

def decorator(func):
    def Inner(*args,**kwargs):
        print("*"*10)
        print(f"The arguments received are {args}")
        result = func(*args, **kwargs)
        print(f"The return value is: {result}")
        print("*" * 10)
        return result
    return Inner


@decorator
def argu(num,strr):
    print(num)
    print(strr)
    return 1
num = int(input("Enter the input 1: "))
strr = input("Enter the input string: ")
argu(num,strr)
