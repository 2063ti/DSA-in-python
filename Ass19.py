
def sum_first_n(n):
    if n==1:
        return 1
    return n + sum_first_n(n-1)

print(sum_first_n(10))

def sum_first_odd_n(n):
    if n==1:
        return 1
    return 2*n-1 + sum_first_odd_n(n-1)

print(sum_first_odd_n(10))

def sum_first_even_n(n):
    if n==1:
        return 1
    return 2*n + sum_first_even_n(n-1)

print(sum_first_even_n(10))
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def sum_of_square_of_n(n):
    if n==1:
        return 1
    return n*n+ sum_of_square_of_n(n-1)

print(sum_of_square_of_n(5))


