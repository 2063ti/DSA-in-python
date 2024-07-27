# print first N natural Numbers.
# 1234...N
# three Steps aproach to solve recursive problems.
# assum that function is ready and giving desired outputPrint(n)1234..N
# print(n-1)think for one small problem
# print(n)
# think for base case  when we don't want to call function n<=0

def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")

printN(9)
def printN1(n):
    if n>0:
        print(n,end=" ")
        printN1(n-1)

print()
printN1(9)

def print_odd(n):
    if n>0:
        print_odd(n-1)
        print(2*n-1,end=" ")
        
print()
print_odd(9)
def print_even(n):
    if n>0:
        print_even(n-1)
        print(2*n,end=" ")
        
print()
print_even(9)

def print_odd_revers(n):
    if n>0:
        print(2*n-1,end=" ")
        print_odd_revers(n-1)
        
        
print()
print_odd_revers(9)
def print_even_revers(n):
    if n>0:
        print(2*n,end=" ")
        print_even_revers(n-1)
        
        
print()
print_even_revers(9)