def arg_decorator(get_argument):
    def check_type(arg):
        print(f"Run function: {get_argument.__name__}, with param: {arg}:")
        try:
            get_argument(arg)
        except TypeError:
            print("String type is not supported")
    return check_type

@arg_decorator
def get_argument(num):
    res = num//2
    print(res)
    return (res)


get_argument(75)
