Problem Domain - Using stacks / queues, write a function that takes in a string, determines if brackets are balanced, and returns a true or false if balances / not balanced. (), [], {}

Input/Output
string - Boolean True or False

Visual
'{}[Fellows](())' -> True
'[({}]' -> False

Big O
time o(n)
space o(n)

Algo
def function -> string
    is the string empty -> return xxxx message
    instan a Stack
    def open bracket array
    dec a close bracket array

    iterate over the string
        check if the char is in the open arr
            if it is create a node and push onto the stack
        check if the char is in the close arr
            temp pop off the stack

            check if the index of what I poped off is the same
            as what I am iterating thouugh
                create node and push back to the stack
                break

    return stack.is_empty() or False

Code
def brackets(text):
    if len(text) > 1:
        retrun 'Empty String Not Allowed'
    stack = Stack()
    accepted_open = ['(', '[', '{']
    accepted_closed = [')', ']', '}']

    for char in text:
        if char in accepted_open:
            stack.push(Node(char))
        elif char in accepted_closed:
            temp = stack.pop()
            if accepted_open[accepted_closed.index(char)] != temp:
                stack.push(Node(char))
                break
    return stack.is_empty or False


Testing
Visual
'{}[Fellows](())' -> True
'[({}]' -> False
