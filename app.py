N = int(input())

number = 0

while N > 0:
    last_digits = N % 10
    N //= 10    # remove last digit

    number = number * 10 + last_digits

print(number, number * 3)


    
