def SumN(n):
    if n == 1:
        return 1
    else:
        s=n+SumN(n-1)
        return s
def SumOdd(n):
    if n==1:
        return 1
    return 2*n-1 + SumOdd(n-1)
def SumEven(n):
    if n==1:
        return 2
    return 2*n + SumEven(n-1)
def SumSquares(n):
    if n == 1:
        return 1
    return n*n + SumSquares(n-1)
print(SumSquares(3))