from math import log10

def count_using_log(n):
    n = abs(n)  # Ensure it works for negative numbers
    if n == 0:
        return 1  # log10(0) is undefined
    return int(log10(n) + 1)

def count_digits(n):
    n = abs(n)  # handle negative numbers
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

user_input = int(input("Enter a Number: "))
print(f"No of digits in {user_input} is: {count_digits(user_input)}")
print(f"(Using log) No of digits in {user_input} is: {count_using_log(user_input)}")
