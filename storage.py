## ******** HOMEWORK #1 =/ #1 MY ANSWER *******************

# a, b = map(float, input('Enter 2 Numbers: ').split())

# print(float(a) + float(b))
# print(float(a) - float(b))
# print(float(a) * float(b))
# print(float(a) / float(b))

## Instructor Answer ************************************
## $$ I didn't fully understand the question*************



# first = input('Enter first number: ')
# first = float(first)

# # let's make it in a single line
# second = float(input('Enter second number: '))

# print(first, '+', second, '=', first + second)
# print(first, '-', second, '=', first - second)
# print(first, '*', second, '=', first * second)
# print(first, '/', second, '=', first / second)

# print("\nEnd of program")

## Homework #1/ problem #2 *** My Answer %%%%%%%%%%%%%%%%%%%%
## Got Quotes around parentheses wrong ********************* 

# name_1 = input("Enter the first student name: ")
# id_1 = input("Enter the first student ID: ")
# grade_1 = input("Enter the first student Grade ")

# name_2 = input("Enter the second student name: ")
# id_2 = input("Enter the second student ID: ")
# grade_2 = input("Enter the second student Grade ")

# avg_grade = (float(grade_1) + float(grade_2)) / 2

# print(str(name_1),(('ID') ,int(id_1)), "got grade", float(grade_1))
# print(str(name_2),(('ID') ,int(id_2)), "got grade", float(grade_2))
# print("Average math grade is ", float(avg_grade))

## Homework #1/ problem #2 *** Instructor Answer %%%%%%%%%%%%

# name1 = input("Enter the first stduent's name: ")
# id1 = input("Enter the first stduent's ID: ")
# grade1 = float(input("Enter the first stduent's grade: "))

# name2 = input("\nEnter the second stduent's name: ")
# id2 = input("Enter the second stduent's ID: ")
# grade2 = float(input("Enter the second stduent's grade: "))

# print('\n\nInformat for students and their "Math" grades')
# msg = name1 + '(ID ' + id1 + ') got grade: ' + str(grade1)
# print(msg)
# msg = name2 + '(ID ' + id2 + ') got grade: ' + str(grade2)
# print(msg)

# average = (grade1 + grade2) / 2.0
# print('Average math grade is', average)

## ***********Homework 1 / problem 3 %% My Answer ** Correc!!!!!

# a, b, c, d, e, f, g, h = map(int, input('Enter 8 numbers: ').split())

# res1 = (int(b) + int(d) + int(f) + int(h))
# res2 = (int(a) + int(c) + int(e) + int(g))

# print(res1, res2)

## Homework 1 / problem 3 %% Instructor Answer ****************
# just create 8 variables, with suitable names for easy coding
# odd1, even1, odd2, even2, odd3, even3, odd4, even4 = map(int, input().split())

# even_sum = even1 + even2 + even3 + even4
# odd_sum = odd1 + odd2 + odd3 + odd4

# print(even_sum, odd_sum)

## Homework 1 / problem 4 %% My Answer% Correct,but not perfect*

# a, b, c = map(str, input('Enter 3 strings: ').split())

# print((str(a) + ("'") + str(b) + ('"') + str(c)) * 10)

## Homework 1 / problem 4 ******** Instructor Answer $$$$$$$$

# A = input()
# B = input()
# C = input()

# combo = A + "'" + B + '"' + C
# combo = combo * 10

# print(combo)

## Homework 3.1 %% Triple Swap My answer $correct$ **********

# num1, num2, num3 = map(int, input().split())

# num4 = num1
# num1 = num2
# num2 = num3
# num3 = num4

# print(num1, num2, num3)

# ## Homework 3.1 %% Triple Swap !! Instructor Answer **********

# num1, num2, num3 = map(int, input().split())

# # one way to swap num1, num2 in 3 lines
# # then swap swap num2, num3 in 3 lines

# # a smarter idea to circulate them (like a circle)

# temp = num1
# num1 = num2
# num2 = num3
# num3 = temp

# print(num1, num2, num3)

## Homework 3.2 Instructors Answer $$$$$$$$$$$$$$$$$$$$$$$

# a, b = map(int, input().split())

# equ_is_1 = a * a
# equ_is_neg_1 = 2 * a + 1

# is_1 = (b + 1) / 2
# is_neg_1 = 1 - is_1

# ans = is_1 * equ_is_1 + is_neg_1 * equ_is_neg_1

# print(ans)

## Homework 3.3 / My Answer / Works Correctly************

# num = int(input())
# ans = (num + 1) * (num / 2)
# print(ans)

## Homework 3.3 / Instructor Answer $$$%$%$%$%$%$%$%$%$%$%$%$%$%$

# n = int(input())
# ans = (n * (n + 1)) / 2
# print(ans)

# Homework Mod.1 // My answer / Very Close to Instructor answer***

# a, b, c, d, e = map(float, input().split())

# avg = (a + b + c + d + e) / 5
# avg2 = (a + b + c) / (d + e)
# avg3 = ((a + b + c) / 3) / ((d + e) / 2)
# print(avg)
# print(avg2)
# print(avg3)
# print(avg2 * 2/3)


# ## Homework MOD.2 // Fractional Part // My Answer // Works WELL
## Identical to Instructor Answer*******************************

# a, b = map(float, input().split())

# res1 = a / b
# res2 = a // b
# res3 = res1 - res2

# print(res3)

# # Homework MOD. 3 . / My Answer OUR REMAINDER / works fairly well

# a, b = map(float, input().split())

# res1 = a / b
# res2 = a // b
# res3 = (res1 - res2) * b

# print(res3)

# Instructor Answer // Better than Mine *********************

# n, m = map(int, input().split())

# # let's try 13/5
# # 13/5 = 2  [2 complete units, each is 5]
# # 2*5 = 10  [total complete units]
# # Reminder is 13-10 = 3. This number generates the fractional part
# result = n - (n // m) * m

# print(result)

#  # Additional NOTES On Previous ****************************

# a, b = map(float, input().split())
# # a = 203 b = 5
# # res = a - (a // b) * b // => Final Solution
# # res = a // b => // 40
# # res = (a // b) * b  // => 200 
# # 203 - 200 => 3
# print(res)

# # MOD MEDIUM // MY ANSWER *** WORKS WELL *****************
# # I INCORRECTLY USED / 10 INSTEAD OF % 10 ****************

# num = int(input())

# is_even1 = num % 2 == 0

# is_even2 = (num / 2) == (num // 2)

# is_even3 = (num / 10) == (num // 10)

# print(is_even1, is_even2, is_even3)

# # INSTRUCTOR ANSWER // MORE COMPLICATED THAN MINE // BETTER????

# num = int(input())


# # Is even using %2
# is_even1 = num % 2 == 0

# # is even using /2
# by2 = num / 2.0         # this is either X.0 or X.5  try 10, 11
# by2 = by2 - int(by2)    # Remove X. This is now either 0 for even or 0.5 for odd
# is_even2 = by2 == 0

# # is even using %10
# last_digit = num % 10	    # even last digit is 0, 2, 4, 6, 8
# is_even3 = last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

# print(is_even1, is_even2, is_even3)

# # HOMEWORK MOD LAST 3 DIGITS SUM// MY ANSWER WORKS WELL******

# num = int(input())

# res1 = num % 10
# num //= 10
# res2 = num % 10
# num //= 10
# res3 = num % 10

# final_res = res1 + res2 + res3

# print(final_res)

# # INSTRUCTOR ANSWER *****************************************8

# n = int(input())

# # remember
# # number % 10   => gets the last digit
# # number // 10  => removes the last digit

# # logic: get digit, remove it. Apply 3 times to get the last 3 digits

# last1 = n % 10
# n = n // 10

# last2 = n % 10
# n //= 10

# last3 = n % 10
# n //= 10

# sum = last1 + last2 + last3
# print(sum)

# # HOMEWORK MOD. MEDIUM. 3 // MY ANSWER LONG BUT WORKS%%%%%%%%%%

# num = int(input())

# res1 = num % 10
# num //= 10
# res2 = num % 10
# num //= 10
# res3 = num % 10
# num //= 10
# res4 = num % 10

# print(res4)

# #INSTRUCTOR ANSWER *** WAY SHORTER AND BETTER **************

# n = int(input())

# # /1000 => removes last 3 digits

# n_without_last_3_digits = n // 1000

# # %10 get digit = 4th
# print (n_without_last_3_digits % 10)

# # HOMEWORK MOD HARD.1 // 100 OR 7 MY ANSWER WORKS WELL *******

# a = int(input())

# res = a % 2
# res2 = (res + 100) - res * 94
# print(res2)

## INSTRUCTOR ANSWER **** NOT SHORTER BUT BETTER THAN MINE

# n = int(input())

# is_even = n % 2 == 0
# is_odd = not is_even

# # formula of 2 parts: only one of them will be activated
# result = is_even * 100 + is_odd * 7

# # In the future, with if condition, you don't need to think in a formula

# print(result)

# # HOMEWORK MOD.HARD.2 // MY ANSWER WORKS WELL *****************

# age = int(input())

# years = age // 360
# months = (age % 360) // 30   DRY : DON'T REPEAT YOURSELF

# days = (age % 360) % 30       DRY: DON'T REPEAT YOURSELF

# print(years, months, days)


# # INSTRUCTOR ANSWER $$$ //  

# days = int(input())

# # By integer division over 360, we know how many 360s in the days
# # Days should be: years * 360 + remaining_days
# # //360 gives the years. %360 remove the year

# years = days // 360
# days = days % 360       # now we remove # of complete years. One easy way is mod

# # same concept as above
# months = days // 30
# days = days % 30

# print(years, months, days)

# # PRACTICE // HOW MANY DIGITS // MY ANSWER // WORKS WELL
# # NEED TO QUIT OVERCOMPLICATING // THINK ABOUT WHAT YOU DON'T 
# # NEED:  TO MUCH REPEATING

# num = int(input())

# if num < 10:
#     print(1, 'digit')
# elif num >= 10 and num < 100:
#     print(2, 'digits')
# elif num >= 100 and num < 1000:
#     print(3, 'digits')
# elif num >= 1000 and num < 10000:
#     print(4, 'digits')
# else:
#     print(5,'+', 'digits')

# # INSTRUCTOR ANSWER // BETTER NO REPEATING **************

# num = int(input())

# if num < 10:
#     print(1, 'digit')
# elif num < 100:
#     print(2, 'digits')
# elif num < 1000:
#     print(3, 'digits')
# elif num < 10000:
#     print(4, 'digits')
# else:
#     print(5,'+', 'digits')

# PRACTICE // SMALLEST OF 3 // INSTRUCTOR ANSWER ***********

# a, b, c = map(int, input().split())

# res = a

# if res > b:
#     res = b

# if res > c:
#     res = c

# print(res)

# # # My Answer for Homework Selection. 1 Easy // Works ********
# # # should have saved is_even to variable see below **********

# a, b = map(int, input().split())

# if a % 2 == 0 and b % 2 == 0:
#     print(float(a) / float(b))

# elif a % 2 != 0 and b % 2 != 0:
#     print(a * b)

# elif a % 2 == 0 and b % 2 != 0:
#     print(a - b)

# else:
#     print(a + b)

# # ## Instructor Answer for Homework Selection. 1 Easy ********


# # a, b = map(int, input().split())

# # is_a_even = a % 2 == 0
# # is_b_even = b % 2 == 0

# # if not is_a_even and not is_b_even:
# #     print(a * b)
# # elif is_a_even and is_b_even:
# #     print(a / b)
# # elif not is_a_even and is_b_even:
# #     print(a + b)
# # else:
# #     print(a - b)

# # Homework Sort 3 Numbers Selection.2 Easy / My Answer/ Correct*
# # Too long *****  Instructors Answer Better for Python *********

# a, b, c = map(int, input().split())

# if a > b:
#     tmp = a
#     a = b
#     b = tmp

# if b > c:
#     tmp = b
#     b = c
#     c = tmp

# if a > b:
#     tmp = a
#     a = b
#     b = tmp

# print(a, b, c)

# # # Homework Sort 3 Numbers Selection.2 Easy / Instructor Ans*


# a, b, c = map(int, input().split())

# # To understand: apply on 3 2 1

# if b < a:  # Swap them:
#     a, b = b, a

# # Now a and b are in correct order: e.g. 2 3 1

# if c < b:  # Swap them
#     b, c = c, b

#     # Now b, are correct
#     # But a, may not be again with b: e.g. 2 1 3

#     if b < a:      # Swap them
#         a, b = b, a

#         # Now 1 2 3

# print(a, b, c)

# # Maximum but Constrained / Selection.3 Easy / My Answer / Works
# # Share this code with Mostafa ******************************!$
# a, b, c = map(int, input().split())
# res = 0

# if a >= 100 and b >= 100 and c >=100:
#     print(-1)
# else:
#     if a < 100:
#         res = a
#     if b < 100 and b > res:
#         res = b
#     if c < 100 and c > res:
#         res = c
    
#     print(res)

# # Instructor Answer #1 Selection. 3 Easy ********************

# a, b, c = map(int, input().split())

# # Assume numbers >= 0
# res = -1
# if res < a < 100:
#     res = a

# if res < b < 100:
#     res = b

# if res < c < 100:
#     res = c

# print(res)

# # test: -10 -20 -30_oop

# # Instructor Answer # 2 / Selection .3 Easy ***********


# a, b, c = map(int, input().split())

# if a >= 100 and b >= 100 and c >= 100:
#     res = -1
# else:
#     # First, find any valid value to initalize
#     if a < 100:
#         res = a
#     elif b < 100:
#         res = b
#     else:
#         res = c

#     if res < a < 100:
#         res = a

#     if res < b < 100:
#         res = b

#     if res < c < 100:
#         res = c

# print(res)

# # test: -10 -20 -30_oop

# # Homework / Selection . 4 / My Answer / Trick Question* 
# # Conditional Statement Was NOT Needed *****************

# x = int(input())
# a, b, c, d, e = map(int, input().split())
# big_cnt = 0
# small_cnt = 0
# if x > a:
#     small_cnt += 1
# else:
#     big_cnt += 1

# if x > b:
#     small_cnt += 1
# else:
#     big_cnt += 1

# if x > c:
#     small_cnt += 1
# else:
#     big_cnt += 1 

# if x > d:
#     small_cnt += 1
# else:
#     big_cnt += 1

# if x > e:
#     small_cnt += 1
# else:
#     big_cnt += 1

# print(small_cnt, big_cnt)

# # Homework / Selection . 4 / Instructor Answer / Trick Question* 

# x, a1, a2, a3, a4, a5 = map(float, input().split())
# cnt = 0

# # We can use if else, but for educational purpose:
# cnt += a1 <= x
# cnt += a2 <= x
# cnt += a3 <= x
# cnt += a4 <= x
# cnt += a5 <= x

# # clearly the 2 values just complement each others
# print(cnt, 5 - cnt)



# # Homework Swlection. 1 Medium ********** Instructor Answer//
#  # Mine was similar but did not work ************************

# # Read first number
# result = float(input())

# # Read other 9 numbers
# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# num = float(input())
# if result < num:
#     result = num

# print(result)

# # Homework // Selection / Medium . 2 // My Answer // Works

# t = int(input())
# cnt = t
# num = int(input())
# cnt -= 1
# res = num

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)

# num = int(input())
# cnt -= 1
# if num > res:
#     res = num
# if cnt == 0:
#     print(res)


# # Homework Selection/ medium . 2 // Instructor Answer *******


# cnt = int(input())

# # read first number
# result = float(input())
# cnt -= 1

# # read UP to 9 times
# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num

# if cnt > 0:
#     num = float(input())
#     cnt -= 1
#     if num > result:
#         result = num


# print(result)


# # # Homework / Selection Intervals / Hard . 1 . My Answer *****
#  # Another trick question / Conditionals not needed ******
# # Insructor Used Boolean Logic Instead // Better than mine

# x, s1, e1, s2, e2, s3, e3 = map(int, input().split())
# cnt = 0

# if x >= s1 and x <= e1:
#     cnt += 1

# if x >= s2 and x <= e2:
#     cnt += 1

# if x >= s3 and x <= e3:
#     cnt += 1

# print(cnt)

# #  Homework / Selection Intervals / Hard . 1 . Instructor.anw

# x, s1, e1, s2, e2, s3, e3 = map(int, input().split())

# #Read start and end, see if X is between them or not, times
# cnt = 0
# cnt += s1 <= x <= e1
# cnt += s2 <= x <= e2
# cnt += s3 <= x <= e3

# print(cnt)

# # Homework Selection / Hard . 2 // My Answer / Works Well***
#  # Instructor Solved without a.b variable ******************
# s1, e1, s2, e2 = map(int, input().split())
# a, b = 0, 0

# if s1 > e2 or s2 > e1:
#     print(-1)

# else:
#     if s1 > s2:
#         a = s1
#     elif s2 > s1:
#         a = s2

#     if e1 < e2:
#         b = e1
    
#     elif e2 < e1:
#         b = e2

# print(a, b)
         
# # Instructor Answer // Less Variables than mine so better!!!!



# s1, e1, s2, e2 = map(int, input().split())

# if e1 < s2 or e2 < s1:
#     print(-1)		# One of them ends before start of the another
# else:
#     if s1 < s2:
#         s1 = s2	    # maximum of (s1, s2)
#     if e1 > e2:
#         e1 = e2	    # minimum of (e1, e2)

#     print(s1, e1)

# # Example of formatted String *************

# num = int(input())
# i = num
# cnt = 1
# if num == 0:
#     cnt = 1 

# elif num < 0:
#     i *= -1

# while i > 0:
#     i //= 10
#     cnt +=1
#     i -= 1

# print(f"# of digits in {num} = {cnt}")

# # Practice // Left Angled Triangle//
# # Note The Printing ****************

# n = int(input())
# i = 1

# while i <= n:
#     cnt = 0
#     while cnt < i:
#         print('*',end ='')
#         cnt += 1
#     print()
#     i += 1

# # # Print Range My Answer *******************

# x, y = map(int, input().split())
# ind = x

# while ind >= x and ind <= y:
#     print(ind)
#     ind += 1

# # # Print Range Instructor Answer **********

# start, end = map(int, input().split())

# while start <= end:
#     print(start)
#     start += 1

# # Repeat Me / My Answer ******************

# s = str(input())
# n = int(input())

# while n > 0:
#     print(s,end='')
#     n -= 1

# # # Repeat Me / Instructor Answer ***********

# n, str = input().split()
# n = int(n)

# while n:
#     print(str, end='')
#     n -= 1

# # Left Angled Triangle / My Answer **********

# n = int(input())

# while n > 0:
#     cnt = n
#     while cnt > 0:
#         print('*',end='')
#         cnt-=1
#     print()    
#     n-=1

# # Left Angled Triangle / Instructor Answer **

# n = int(input())

# row = n
# while row > 0:
#     stars_count = 1

#     while stars_count <= row:
#         print('*', end='')
#         stars_count += 1

#     print()
#     row -= 1

# # Special Average // My Answer **************************************

# odd_sum, even_sum, odd_cnt, even_cnt = 0, 0, 0, 0
# n = int(input())

# i = 0
# while i < n:
#     x = float(input())
#     i += 1
    
#     if i % 2 != 0:
#         odd_sum += x
#         odd_cnt += 1
        
#     elif i % 2 == 0:
#         even_sum += x
#         even_cnt += 1

# print(odd_sum / odd_cnt, even_sum / even_cnt)

# # Special Average / Instructors Answer *******************************

# even_sum, odd_sum, even_count, odd_count = 0, 0, 0, 0
# n = int(input())

# cnt = 1
# while cnt <= n:
#     value = float(input())

#     if cnt % 2 == 0:    # even position
#         even_sum += value
#         even_count += 1
#     else:               # odd position
#         odd_sum += value
#         odd_count += 1

#     cnt += 1

# print(odd_sum / odd_count, even_sum / even_count)

# # Application #1 // It works, but some things I don't know how to do!

# n = int(input("Press 1 to begin"))
# while n != 3:
#     print("Menu:")
#     print("Enter 1 to sum numbers from 1 to N")
#     print("Enter 2 to evaluate simple 2 number expression (e.g. 2 + 3")
#     print("Enter 3 to End the Program")
#     n = int(input())

#     if n < 0 or n > 3:
#         print("Invalid Input...Try Again")

#     if n == 1:
#         a = int(input())
#         print(a * (a + 1) / 2)
#         continue

#     if n == 2:
#         print("Enter a simple expression")
#         x = input()
#         print(f"Expression value is {x}")
#         continue

#     if n == 3:
#         print()
#         break
# print("End of Program")

# # Application #1 // Instructors Solution *****************************

# while True:
#     print('\n\nMenu:')
#     print('Enter 1 to sum numbers 1 to N')
#     print('Enter 2 to evaluate simple 2 numbers expression (e.g. 2+3')
#     print('Enter 3 to end the rogram')

#     user_inp = input("\nEnter Choice from 1 to 3: ")
    
#     if user_inp !='1' and user_inp != '2' and user_inp != '3':
#         print('Invalid Input...Try again')
#         continue
    
#     if user_inp == '1':
#         n = int(input('Enter a number: '))
#         sum = (n * (n + 1))//2
#         print('Sum from 1 to', n, 'is', sum)
#     elif user_inp == '2':
#         num1, operation, num2 = input('Enter a simple expression: ').split()
#         num1, num2 = float(num1), float(num2)

#         result = None

#         if operation == '+':
#             result = num1 + num2
#         elif operation == '-':
#             result = num1 - num2
#         elif operation == '*':
#             result = num1 * num2
#         elif operation == '**':
#             result = num1 ** num2
#         else:
#             if num2 == 0:
#                 print('Not a valid operation!')
#             elif operation == '/':
#                 result = num1 / num2
#             else:
#                 result = num1 // num2
        
#         if result != None:
#             print('Expression value is ', result)
#     else:
#         break

# # Homework While Loops Medium // My Answer // Print a Diamond ******
# # Mine // Works but there are way too many variables not efficient ***

# n = int(input())
# cnt = 1
# x = n
# cnt2 = n * 2 -1
# spcs = 0
# while n > 0:
#     strs_cnt = 0
#     spc_cnt = n - 1
    
#     while spc_cnt > 0:
#         print(' ',end='')
#         spc_cnt -= 1
    
#     while strs_cnt < cnt:
#         print('*',end='')
#         strs_cnt += 1
#     print()
#     cnt += 2
#     n -= 1

# while x > 0:
#     strs_cnt = 0
#     spc_cnt = 0
    
#     while spc_cnt < spcs:
#         print(' ',end='')
#         spc_cnt +=1

#     while strs_cnt < cnt2:
#         print('*',end='')
#         strs_cnt += 1
    
#     print()
#     spcs +=1
#     cnt2 -= 2
#     x -= 1

# # Instructor Answer // Print A Diamond // Way Better than mine ******


# n = int(input())


# row = 1
# while row <= n:
#     # Print N - rows spaces
#     stars_count = 1
#     while stars_count <= n - row:
#         print(' ', end='')
#         stars_count += 1

#     # Print 2*rows-1 spaces
#     stars_count = 1
#     while stars_count <= 2 * row-1:
#         print('*', end='')
#         stars_count += 1

#     print()
#     row += 1


# row = n
# while row > 0:
#     # Print N - rows spaces
#     stars_count = 1
#     while stars_count <= n - row:
#         print(' ', end='')
#         stars_count += 1

#     # Print 2*rows-1 spaces
#     stars_count = 1
#     while stars_count <= 2 * row-1:
#         print('*', end='')
#         stars_count += 1

#     print()
#     row -= 1

# # Homework While Loops multiples // My Answer // Works Well ********

# n = int(input())
# num = 0
# while num <= n:
#     if num % 3 == 0 and num % 4 == 0 or num % 8 == 0:
#         print(num, end=' ')
#     num +=1

# # While loops Multiples // Instructor Answer ***************************

# n = int(input())

# cnt = 0

# while cnt <= n:
#     if cnt % 8 == 0 or cnt % 3 == 0 and cnt % 4 == 0:
#         print(cnt, end=' ')

#     cnt += 1

# # Homework While Loops Medium / Special Multiples 2 / My Answer ******

# num = int(input())
# x = 0
# while(num > 0):
#     x += 1
#     if(x % 3 == 0 and x % 4 != 0):
#         print(x, end=' ')
#         num -= 1


# ## Homework While Loops Medium / Special Multiples 2 / Instructor ******

# n = int(input())

# cnt = 0
# current_number = 0

# while cnt < n:
#     if current_number % 3 == 0 and current_number % 4 != 0:
#         print(current_number, end=' ')
#         cnt += 1

#     current_number += 1

# # Homework While Loops / Minimum of Values / My Answer / works / I 
# # But I only wanted to use two loops / couldn't figure it out

# test = int(input())

# while test > 0:
#     n = int(input())
#     test -= 1
#     ans = 0
#     while n > 0:
#         x = int(input())
#         n -= 1
#         ans = x
        
#         while n > 0:
#             y = int(input())
#             n -= 1
#             if y <= x:
#                 ans = y
    
#     print(f"Min value is {ans}")

# # Instructor Answer with Only two loops ****************************
# 
# total_cases = int(input())

# # Outer loop for cases
# while total_cases > 0:
#     numbers_cnt = int(input())

#     pos = 0
#     result = 0

#     # Inner loop to read a case
#     while pos < numbers_cnt:
#         value = int(input())

#         if pos == 0:
#             result = value
#         elif result > value:
#             result = value

#         pos += 1

#     print('Min value is:', result)
#     total_cases -= 1    
    

# #Homework While Loops Hard // My Answer // Didnt work / Study syntax!!!!!!!!!!!!!!!!!!!!!!!!

# n = int(input())

# while n > 0:
#     phr = str(input())
#     n-=1
    

#     if phr == 'no' or 'No' or 'NO' or 'nO' or 'on' or 'On' or 'ON' or 'oN':
#         ans = phr
#         print(ans)

# #Homework While Loops Hard // Instructor Answer ^^^^^^^^^^^^^^^^^^^^^^^^^^

# total_cases = int(input())

# pos = 0

# while pos < total_cases:
#     str = input()

#     # there are 8 different ways to make 2 letters no in lower/upper cases
#     if str == "no" or str == "No" or str == "nO" or str == "NO" or \
#         str == "on" or str == "oN" or str == "On" or str == "ON":
#         print('Match:', str)

#     pos += 1

# # # Homework While LOops Hard #2 // Couldn't Solve *********
# # #!!!!!!!!!!!!!!!!!!!!!!!! This one is really Cool!!!!!!!!!
# N = int(input())

# number = 0

# while N > 0:
#     last_digits = N % 10
#     N //= 10    # remove last digit

#     number = number * 10 + last_digits    N = 321 number => 1 / 12 / 123

# print(number, number * 3)

# # TEST LINE FOR NEXT COMMITT // TRYING TO PUSH

# # Homework While Loops Hard / Multiplication Table / My Answer****

# N, M = map(int, input().split())
# x = 1

# while x <= N:
#     y = 1
#     while y <= M:
#         print(x, 'x', y, '=', (x*y))
#         y += 1
#     x+=1

# # Multiplication Table Instructors Answer
# # Exactly The Same as mine !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# n, m = map(int, input().split())

# cnt_n = 1

# # first col loop
# while cnt_n <= n:
#     cnt_m = 1

#     # second col loop
#     while cnt_m <= m:
#         print(cnt_n, " x ", cnt_m, " = ", cnt_n * cnt_m)
#         cnt_m += 1

#     cnt_n += 1

# # While Loops Hard: Special Sum / My Answer Take 1

# T = int(input())

# while T > 0:
#     N = int(input())
#     T -= 1
#     cnt = 1
#     ans = 0
#     while N > 0:
#         num = int(input())
#         N -= 1
#         i = 1
#         res = 1
#         while i <= cnt:
#             res *= num
#             i += 1
#         cnt += 1
#         ans += res
#     print(ans)

# # # While Loops Hard: Special Sum / My Answer Take 1
# # Identical to Instructors Answer

# T = int(input())

# while T > 0:
#     N = int(input())
#     T -= 1
#     cnt = 1
#     ans = 0
#     while N > 0:
#         num = int(input())
#         N -= 1
#         i = 1
#         res = 1
#         while i <= cnt:
#             res *= num
#             i += 1
#         cnt += 1
#         ans += res
#     print(ans)

# # # While Loops 4 hard// Instructor Answer // Special Sum**************************
# # We need 3 nested loops
# # loop over test cases
# #   loop over reading numbers
# #       loop to repeat the number K times (multiplication)


# T = int(input())
# # Loop on cases
# while T > 0:
#     N = int(input())
#     cnt_N, sum = 1, 0

#     # loop over reading a case
#     while cnt_N <= N:
#         value = int(input())
#         cnt_deep, result = cnt_N, 1

#         # Loop to compute the sum: a, b*b, c*c*c, d*d*d*d, e*e*e*e*e……
#         while cnt_deep > 0:
#             result *= value
#             cnt_deep -= 1

#         sum += result
#         cnt_N += 1

#     print('Sum is', sum)
#     T -= 1


# """
# input
# 2
# 3   
# 5 
# 7 
# 2
# 4  
# 1 
# 2 
# 3 
# 4


# # Practice / Special Sum Repeated With for loop *******

# total_cases = int(input())

# for case in range(total_cases):
#     N, sum = int(input()), 0

#     for pos in range(N):
#         value, result = int(input()), 1

#         for it in range(pos + 1):
#             result *= value
#         sum += result
#     print('Sum is', sum)

# # Practice / Pair of Numbers / My Answer *********
# # Same As Instructors*****************************

# N, M, sum = map(int, input().split())
# res = 0

# for a in range(1, N+1):
#     for b in range(1, M, 1):
#         if a + b == sum:
#             res +=1
# print(res)