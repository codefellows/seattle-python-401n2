## Overview of today's warm-up challenge

Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.

```python

# Iterative
def add_it_up_int(n):
    if type(n) != int: 
        return 0
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum


# Recursive
def add_it_up_rec(n):
    if type(n) != int: 
        return 0
    if n <= 1:
        return 1
    return n + add_it_up_rec(n - 1)

```
