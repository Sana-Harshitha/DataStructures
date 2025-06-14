user_input=int(input("Enter a Number: "))

num=user_input
while num >0 :
    last_digit = num % 10
    print(last_digit)
    num=num//10