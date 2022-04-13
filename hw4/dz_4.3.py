def cache_decorator(func):
    cache = {}
    counters = {}
    hits = {}

    def cache_func(*args):
        counters[func] = counters.get(func, 0) + 1
        if args in cache:
            hits[func] = hits.get(func, 0) + 1
            print(f"Used cache with counter = {counters[func]} and hits = {hits[func]}")
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            print(f"Function executed with counter = {counters[func]}, function result = {res}")
            return res

    return cache_func


@cache_decorator
def function_res(a, b):
    return a + b


function_res(4, 7)
function_res(4, 8)
function_res(4, 9)
function_res(4, 9)
function_res(3, 9)
function_res(4, 9)
function_res(4, 9)


