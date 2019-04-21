"""
    Co routines are made with the same yield function as in generators. But the main difference is that co routine
    actually consumes values while generators generate values. Co routines specifically are function that can
    suspend and resume its execution at well defined locations in a code.

    yield: Used to suspend a co routine
    send: This is used to pass data to a co routine, and hence resume execution
    close: This is used to close a co routine
"""


# Calling next everytime after creating a co routine in annoying so we create a decorator
def co_routine(fn):
    def wrapper(*args, **kwargs):
        c = fn(*args, **kwargs)
        next(c)
        return c

    return wrapper


@co_routine
def string_match(string):
    print(f"Co routine ready to match any string with value {string}")
    try:
        while True:
            text = yield  # Suspend and wait for value
            if text == string:
                print("Yes matched")
    except GeneratorExit:  # On getting close signal , stop the co routine
        print("Closing the awesome co routine")


# Note run this through the shell
f = string_match("Test")
f.send("yo")
f.send("test")
f.close()
