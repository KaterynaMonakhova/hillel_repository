def arg_decorator(func):
    def check_arg(*arg):
        print("Enter the one integer: ")
        try:
            print(f"x = {func(*arg)}")
        except ValueError:
            print("string type is not supported")

    return (check_arg)


@arg_decorator
def get_argument():
    x = int(input())

    return x


get_argument()
