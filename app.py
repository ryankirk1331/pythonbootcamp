# # For Loops / Digits Sum / My Answer / Doesn;t work at all !!!!!!!!!
# # I Saved it just to compare Logic between it and working code!!!!!!

# n, a, b = map(int, input().split())
# ans = 0
# c = 0
# res = 0
# for i in range(1, n+1):
#     if i < 10 and i >= a and i <= b:
#         ans += i
#     elif i >= 10:
#         while i > 0:
#             c = i % 10
#             i //= 10
#             res +=c 
#             if res >= a and res <= b:
#                 ans += i
# print(ans)

#  # Instructors Answer **********************************************

# n, a, b = map(int, input().split())
# total = 0

# for i in range(1, n+1):
#     tmp = i     # be careful - take copy
#     digits_sum = 0

#     while tmp > 0:
#         digits_sum += tmp % 10
#         tmp //= 10

#     if a <= digits_sum <= b:
#         total += i

# print(total)