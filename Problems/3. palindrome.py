user_input = int(input("Enter a Number: "))
def palindrome_check(user_input):
    num = user_input
    result = 0
    while num > 0:
        id = num % 10
        result =result*10 + id
        num //= 10
    return result==user_input
if palindrome_check(user_input):
    print(f"Your Entered Number is a Palindrome")
else:
    print(f"Your Entered Number is Not a Palindrome")
