def brackets(text):
    if len(text) < 1:
        return 'Empty String Not Allowed'
    stack = []
    accepted_open =   ['(', '{','[']
    accepted_closed = [')', '}',']']

    for char in text:
        if char in accepted_open:
            stack.append(char)
        elif char in accepted_closed:
            temp = stack.pop()
            if accepted_open[accepted_closed.index(char)] != temp:
                print('char eq' + accepted_open[accepted_closed.index(char)])
                print('pop from stack' + temp)
                stack.append(temp)
    return len(stack) == 0 or False


# print(brackets(''))
# print(brackets('test'))
# print(brackets('{{}}'))
# print(brackets('{{}}(){{}}'))
# print(brackets('()[[Extra Characters]]'))
# print(brackets('(){{}}[[]]'))
# print(brackets('{{}}{{Code}}[Fellows](())'))

# print(brackets('(((([)])))'))
# print(brackets('[({{}}]'))
# print(brackets('(]('))
print(brackets('{(})'))
# print(brackets('{'))
# print(brackets('}'))


