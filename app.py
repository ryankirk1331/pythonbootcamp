# # Practice / Pair of Numbers / My Answer *********

N, M, sum = map(int, input().split())
res = 0

for a in range(1, N+1):
    for b in range(1, M, 1):
        if a + b == sum:
            res +=1
print(res)
