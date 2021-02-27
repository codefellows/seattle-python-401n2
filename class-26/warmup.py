# Write a function that will reverse a list without using ANY builtin methods

def reverse(our_list):
    left = 0
    right = len(our_list) -1
# Loop to get to last index and store

    while left < right:

        # our_list[left], our_list[right] = our_list[right], our_list[left]

        temp = our_list[left]
        our_list[left] = our_list[right]
        our_list[right] = temp

        left += 1
        right -= 1

    return our_list    

our_list = [1, 2, 3, 4, 5, 6]
print(reverse(our_list))
