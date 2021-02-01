n = int(input())
num = 0
while num <= n:
    if num % 3 == 0 and num % 4 == 0 or num % 8 == 0:
        print(num, end=' ')
    num +=1
