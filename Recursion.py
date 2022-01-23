#n! = 1*2*3*......*n
#n! = [1*2*3*......n_1]*n
#n! = n*(n_1)!


def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
print(factorial_iter(4))

def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    return n* factorial_recursion(n-1)
print((factorial_recursion(5)))