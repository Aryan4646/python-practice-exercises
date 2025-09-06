# GCD of two numbers

# Using prime factorization
# def gcd(n1,n2):
#     gcd = 1
#     smaller_num = n1 if n1<n2 else n2
#     i = 2
#     while smaller_num >= i:
#         while n1%i == 0 and n2%i ==0:
#             gcd *= i
#             n1 //=i
#             n2 //= i
#             smaller_num //=i
#         else:
#             i+=1
#     return gcd

# different approach
# def gcd(n1,n2):
#     gcd = 1
#     smaller_num = n1 if n1<n2 else n2
#     for i in range(2,smaller_num+1):
#         if n1%i == 0 and n2%i ==0:
#             gcd = i
#     return gcd

# Using euclidean algorithm

def gcd(a,b):
    if a>b:
        if b == 0:
            return a
        else:
            return gcd(b,a%b)
    else:
        if a == 0:
            return b
        else:
            return gcd(a,b%a)

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))


print(f"Gcd of {num_1} & {num_2}: {gcd(num_1,num_2)}")