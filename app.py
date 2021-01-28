x = int(input())
a, b, c, d, e = map(int, input().split())
big_cnt = 0
small_cnt = 0
if x > a:
    small_cnt += 1
else:
    big_cnt += 1

if x > b:
    small_cnt += 1
else:
    big_cnt += 1

if x > c:
    small_cnt += 1
else:
    big_cnt += 1 

if x > d:
    small_cnt += 1
else:
    big_cnt += 1

if x > e:
    small_cnt += 1
else:
    big_cnt += 1

print(small_cnt, big_cnt)