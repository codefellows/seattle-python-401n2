# Is that number divisible by 3 return Fizz
# Is that number divisible by 5 return Buzz
# Is that number divisible by 3 and 5 return FizzBuzz
# If that number is not divisible by 3 or 5 return the number

# def fizz_buzz(num):
#
#     if not num % 15:
#         return 'FizzBuzz'
#     elif not num % 3:
#         return 'Fizz'
#     elif not num % 5:
#         return 'Buzz'
#     else:
#         return num


# def fizz_buzz(n):
#   if not n % 15: # if no remainder
#     return 'FizzBuzz'
#   elif not n % 3:
#     return 'Fizz'
#   elif not n % 5:
#     return 'Buzz'
#   else:
#     return n

# def fizz_buzz(num):
#     for n in range(1, num+1):
#         return int("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n)


# def fizz_buzz(num):
#     if not (num % 3):
#         if not (num % 5):
#             return 'FizzBuzz'
#         else:
#             return 'Fizz'
#     elif not (num % 5):
#         return 'Buzz'
#     else:
#         return num

#
# def fizz_buzz(num):
#     word = ''
#     if num % 3 == 0:
#         word = 'Fizz'
#
#     if num % 5 == 0:
#         word += 'Buzz'
#
#     return word or num

# def fizz_buzz(num):
#     return 'FizzBuzz' if not num % 15 else 'Fizz' if not num % 3 else 'Buzz' if not num % 5 else num

name = 'Thomas'
age = 32

# print(name + ' is ' + age + 'years old')

print(f'{name} "is" {age} years old')

