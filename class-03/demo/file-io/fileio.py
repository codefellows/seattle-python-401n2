#
# file = open('assets/spam.txt')
# print(file)
#
# contents = file.read()
# print(contents)
#
# print('Is the file closed?', file.closed)
#
# file.close()
# print('Is the file closed?', file.closed)


# with open('assets/spam.txt') as file:
#     print(file.read())
#
# print('Is the file closed?', file.closed)

# help(file)


with open('assets/brain.jpg', 'rb') as f:
    contents = f.read()

for x in contents[:128]:
    print(type(contents))

trimmed = contents[:len(contents) // 2]

with open('assets/brain1.jpg', 'wb') as f2:
    f2.write(trimmed)

