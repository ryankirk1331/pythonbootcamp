num = int(input())
i = num
cnt = 1
if num == 0:
    cnt = 1 

elif num < 0:
    i *= -1

while i > 0:
    i //= 10
    cnt +=1
    i -= 1

print(f"# of digits in {num} = {cnt}")

         