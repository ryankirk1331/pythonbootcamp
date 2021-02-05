# # For Loops / Find Special Pairs Slow / My Answer / Tiny Bit of Help.

# cnt = 0
# for x in range(50, 301, 1):
#     for y in range(70, 401, 1):
#         if x < y and (x + y) % 7 == 0:
#             cnt += 1
        
# print(cnt)

# #  For Loops / Find Special Pairs Efficient / My Answer **************

cnt = 0
for x in range(50, 301, 1):
    for y in range(70, 401, 1):
        if x < y and (x + y) % 7 == 0:
            cnt += 1
        
print(cnt)