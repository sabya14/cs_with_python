"""
    Any function with a yield function makes a generator function, which returns a generator object.
    We can call next on it to get the value. Its a fast way to create iterators
"""


def generators():
    print("Start generator")
    for i in range(3):
        print(f"Before yielding {i}")
        yield i
        print(f"After yielding {i}")


f = generators()

for i in f:
    print(i)
