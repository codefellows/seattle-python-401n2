from collections import Counter

counter = Counter((1, 2, 3, 4, 5, 6))

# print(counter)
# Counter({1: 3, 3: 2, 6: 1})

# counter = Counter((1, 2, 3, 4, 5, 6))

# print(counter[1])

print(len(counter.most_common()))
# [(1, 3), (3, 2), (6, 1)]

# print(counter.most_common()[0][1])
