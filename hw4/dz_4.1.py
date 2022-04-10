def division_decorator(func):
    def check_division():
        print("Enter the one integer: ")
        try:
            func()
        except ValueError:
            raise ValueError("string type is not supported")

        return (check_division)


@division_decorator
def get_argument(x):
    x = input()

    return (int(input()))


get_argument()
