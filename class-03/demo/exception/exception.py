#
#
# print("let's do something totally wrong. See if you can spot me in the output!")
# print("Too many parentheses")
#
# print("More wrongness. Do I get printed?")
# print("Who has ever ' messed up ' quotations marks?")

# print("What happens now? Do you see me printed?")
# print('We got this one as well')
# value = 1/0
# print('after the error')

try:
    print("Divide by zero again", 1 / 0)
except ZeroDivisionError:
    print("Don't divide by zero silly.")
except TypeError:
    print('This is a Type Error.  Check input')
finally:
    print('This will always run')

# print("handled the exception above, carrying on")

# age = 18
#
# if age < 21:
#     raise ValueError("Invalid age - No Drinking for you!")


# class SocialDistanceError(Exception):
#     def __init__(self, distance):
#         super().__init__(f'Stay 6 feet away, not {distance}')
#
#
# distance_feet = 4
#
# if distance_feet < 6:
#     raise SocialDistanceError(distance_feet)
