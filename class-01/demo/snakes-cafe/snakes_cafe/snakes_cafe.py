# list , dictionary

def snakes():

    orders = {
        'wings': 0,
    }

    print(orders)

    print('Welcome to Snakes Cafe')
    wing_order = orders['wings']

    user_input = input('Please enter a item to order: ')

    print(user_input)

    print(orders['wings'])

    orders['wings'] += 1

    print(orders)


if __name__ == '__main__':
    snakes()
