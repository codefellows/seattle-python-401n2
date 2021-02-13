from test_demo.primary import call_other_function

def test_call_other_function():
    actual = call_other_function()
    expected = 2
    assert actual == expected
