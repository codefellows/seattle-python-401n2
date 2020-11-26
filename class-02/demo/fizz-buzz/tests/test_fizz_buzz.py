from fizz_buzz import __version__


from fizz_buzz.fizz_buzz import fizz_buzz

def test_version():
    assert __version__ == '0.1.0'



def test_one():
    actual = fizz_buzz(1)
    expected = '1'
    assert actual == expected


def test_two():
    actual = fizz_buzz(2)
    expected = '2'
    assert actual == expected


def test_three():
    actual=fizz_buzz(3)
    expected='Fizz'
    assert actual == expected

def test_four():
    actual=fizz_buzz(4)
    expected='4'
    assert actual == expected

def test_five():
    actual=fizz_buzz(5)
    expected='Buzz'
    assert actual == expected

def test_six():
    actual=fizz_buzz(6)
    expected='Fizz'
    assert actual == expected

def test_ten():
    actual=fizz_buzz(10)
    expected='Buzz'
    assert actual == expected

def test_15():
    actual=fizz_buzz(15)
    expected='FizzBuzz'
    assert actual == expected


def test_thirty():
    actual=fizz_buzz(30)
    expected='FizzBuzz'
    assert actual == expected


















# def test_one():
#     actual = fizz_buzz(1)
#     expected = '1'
#     assert expected == actual

# def test_two():
#     expected = 2
#     actual = fizz_buzz(2)
#     assert expected == actual

# def test_three():
#     expected = 'Fizz'
#     actual = fizz_buzz(3)
#     assert expected == actual

# def test_four():
#     expected = 4
#     actual = fizz_buzz(4)
#     assert expected == actual

# def test_five():
#     expected = 'Buzz'
#     actual = fizz_buzz(5)
#     assert expected == actual

# def test_fifteen():
#     expected = 'FizzBuzz'
#     actual = fizz_buzz(15)
#     assert expected == actual

# def test_fizz_buzz_range():
#     expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
#     actual = fizz_buzz_sequence(range(1,15 + 1))
#     assert expected == actual

# def test_fizz_buzz_list():
#     expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz',11,'Fizz',13,14,'FizzBuzz']
#     actual = fizz_buzz_sequence([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
#     assert expected == actual

# def test_fizz_buzz_dict():
#     expected = {
#         1:1,
#         2:2,
#         3:'Fizz',
#         4:4,
#         5:'Buzz',
#         15:'FizzBuzz'
#     }

#     actual = fizz_buzz_dict([1,2,3,4,5,15])

#     assert expected == actual
