from test_demo.other import other_function
# from other import other_function

def primary_function():
    num = 1
    print(num)
    return num


def call_other_function():
    return(other_function())


if __name__ == "__main__":
    primary_function()
    call_other_function()


















# [run]
# omit=
#     .venv/*

# coverage run -m pytest
# coverage report