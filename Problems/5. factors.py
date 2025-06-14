from math import sqrt

user_input=int(input("Enter a Number: "))

#Brute Force
def factor_v1(num):
    result=[]
    for i in range(1,num+1):
        if num % i==0:
            result.append(i)
    return result

#Better Soultion
def factor_v2(num):
    result=[]
    for i in range(1,num//2 + 1):
        if num % i==0:
            result.append(i)
    result.append(num)
    return result

#Optimal Solution
def factor_v3(num):
    result=[]
    for i in range (1,int(sqrt(num)+1)):
        if num % i ==0:
            result.append(i)
        if num // i != i :
            result.append(num//i)
    result.sort()
    return result

print(factor_v1(user_input))
print(factor_v2(user_input))
print(factor_v3(user_input))