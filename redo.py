## ***** After Completing Functions Section Revisit *********** Saturday Feb 13

# For Loops Practice Last Probem
# For Loops Homework # 2 / Make it more efficient
# For Loops Homework #5 / Print Primes
# For Loops Homework # 6

#  #redo of For Loops Practice / Last Problem!!! / Instructor answer repeat again!!!!!

# n, m, w = map(int, input().split())
# cnt = 0
# for a in range(1, n+1):
#     for b in range(a, m+1):
#         c = a + b

#         if 1 <= c <= w:
#             cnt += w - c + 1

# # For Loops / Homeworks 2 Redo / Failed REPEAT again ***********************************

# cnt = 0
# for x in range(50, 301):
#     start = max(70, x + 1)
#     for y in range(start, 401):
#         if (x + y) % 7 == 0:
#             cnt += 1
# print(cnt)

# # For Loops / Homework 3 Redo / MY ANSWER / WORKS NO REPEAT**************************

# cnt = 0
# for a in range(1, 200+1):
#     for b in range (1, 201):
#         for c in range(1, 201):
#             d = a + b - c

#             if 1 <= d <= 200:
#                 cnt += 1
# print(cnt)

# # FOR LOOPS HOMEWORK # 5 / REDO / Instructor Answer Repeat Again **********************

# n = int(input())

# for i in range(3, n+1):
#     is_ok = True
        
#     for j in range(2, i):
#         if i % j == 0:
#             is_ok = False
#             break

#     if is_ok:
#         print(i,end=' ')

# # For Loops Homework # 6 / REDO / Instructor Answer REDO Again **********************


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
# # ***********************************************************************************

# REDO on Saturday FEB 20

# Functions Homework Problem #1
# Functions Homework Problem #2
# Functions Homework Problem #3
# Functions Homework Problem #4
# Objects and Classes Prolem #2
# Objects and Classes Problem #3
# Objects and Clases Problem #4
# For Loops Practice Last Probem
# For Loops Homework # 2 / Make it more efficient
# For Loops Homework #5 / Print Primes
# For Loops Homework # 6
# # **********************************************************************************