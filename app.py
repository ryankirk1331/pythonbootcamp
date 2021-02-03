T = int(input())

while T > 0:
    N = int(input())
    T -= 1
    cnt = 1
    ans = 0
    while N > 0:
        num = int(input())
        N -= 1
        i = 1
        res = 1
        while i <= cnt:
            res *= num
            i += 1
        cnt += 1
        ans += res
    print(ans)