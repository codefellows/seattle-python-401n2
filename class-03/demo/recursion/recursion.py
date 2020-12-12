def recursive_function(num):

    if num <= 1:
        return 1

    return num * recursive_function(num - 1)


print(recursive_function(5))


#                 return 1
#             return 2 * recursive_function(2 - 1) = return 2 * 1
#         return 3 * recursive_function(3 - 1) = return 3 * 2
#     return 4 * recursive_function(4 - 1) = return 4 * 6
# return 5 * recursive_function(5 - 1) = return 5 * 24

