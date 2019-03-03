import functools


def test(a, b=10):
    print("A:", a)
    print("B:", b)


def show_details(name, func, is_partial=False):
    print(name)
    if not is_partial:
        print("Not partial")
        print(func.__name__)
    if not is_partial:
        print(func.__name__)
    else:
        print("Partial")
        print(func.func)
        print(func.args)
        print(func.keywords)


# normal test show details
show_details("Normal", test)
test(3)

# Now we create a function with smaller args than the original test function.
test_with_fixed_a = functools.partial(test, 1)
test_with_fixed_a(b=12)
