from random import randint
def division_decorator(func):
    def check_division(arg):
        result = 100 % (func(arg))
        print(f"Run function: {func.__name__}, with param: {arg}:")
        print("We are OK!") if result == 0 else print(f"Bad news guys, we got {result}")
    return (check_division)

@division_decorator
def get_division(num):
    return num


get_division(randint(1, 11))

