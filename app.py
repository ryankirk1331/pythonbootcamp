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

num = int(input())

if num < 10:
    print(1, 'digit')
elif num < 100:
    print(2, 'digits')
elif num < 1000:
    print(3, 'digits')
elif num < 10000:
    print(4, 'digits')
else:
    print(5,'+', 'digits')