import sys

def main():
    name = input('Please Enter your Name: ')
    print(f'{name}, please press q to quit!')
    end_game = input('> ')
    if end_game == 'q':
        quit_game()
    else:
        print('You do not listen very well')

def quit_game():
    sys.exit('Thanks for Playing.  YOu has xx rolls with a xx score')


if __name__ == "__main__":
    main()
