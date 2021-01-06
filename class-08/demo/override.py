import builtins

print('Enter your Name ')


def mock_print(*args):
    input('Input Something Here --> ')


real_print = builtins.print

builtins.print = mock_print


print('Enter your Name')


real_print('Enter your Name ')

builtins.print = real_print

print('Please Please enter your name this time: ')
