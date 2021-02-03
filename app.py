n = int(input())
cnt = 0
while n > 0:
    last_digit = n % 10
    n //= 10
    cnt += 1
    n -= 1
print(cnt)
    
