# a generator function to yield even numbers up to a given limit.

def generatorr(n):
    i = 0
    while i < n:
        yield i
        i += 2


num = int(input("Enter the number: "))

gen = generatorr(num)

for even in gen:
    print(even)