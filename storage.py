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

