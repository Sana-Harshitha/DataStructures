def armstrong_check(n):
    num = n
    no_of_digits = len(str(n))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** no_of_digits
        num //= 10
    return total == n

user_input = int(input("Enter a Number: "))
if armstrong_check(user_input):
    print("Your Entered Number is an Armstrong Number")
else:
    print("Your Entered Number is Not an Armstrong Number")
