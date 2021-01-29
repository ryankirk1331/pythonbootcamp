s1, e1, s2, e2 = map(int, input().split())
a, b = 0, 0

if s1 > e2 or s2 > e1:
    print(-1)

else:
    if s1 > s2:
        a = s1
    elif s2 > s1:
        a = s2

    if e1 < e2:
        b = e1
    
    elif e2 < e1:
        b = e2

print(a, b)
         