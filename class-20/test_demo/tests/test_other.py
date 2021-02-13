from test_demo.other import other_function

def test_other_function():
    actual = other_function()
    expected = 2
    assert actual == expected
