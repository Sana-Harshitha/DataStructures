def printN_Rev(n):
    if n>0:
        print(n) #reverse number
        printN_Rev(n-1)
        # print (n)
def printN(n):
    if n>0:
        printN(n-1)
        print (n)
def printN_odd(n):
    if n>0:
        printN_odd(n-1)
        print (2*n-1,end=' ')
def printN_even(n):
    if n>0:
        printN_even(n-1)
        print (2*n,end=' ')
def printN_odd_Rev(n):
    if n>0:
        print (2*n-1,end=' ')
        printN_odd_Rev(n-1)
def printN_even_Rev(n):
    if n>0:
        print (2*n,end=' ')
        printN_even_Rev(n-1)
printN_odd(5)