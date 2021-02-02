test = int(input())

while test > 0:
    n = int(input())
    test -= 1
    ans = 0
    while n > 0:
        x = int(input())
        n -= 1
        ans = x
        
        while n > 0:
            y = int(input())
            n -= 1
            if y <= x:
                ans = y
    
    print(f"Min value is {ans}")
    