import datetime


def co_routine(fn):
    def wrapper(*args, **kwargs):
        f = fn(*args, **kwargs)
        next(f)
        return f

    return wrapper


@co_routine
def grep(substring, child_f):
    try:
        while True:
            text = (yield)  # Get data from the read line function
            child_f.send(text.count(substring))  # pass it on to the child routine, i.e count
    except GeneratorExit:
        print("Exiting")


@co_routine
def count():
    n = 0
    try:
        while True:
            n += (yield)
    except GeneratorExit:
        print("Substring count", n)


def read_line(read_lines, word_to_search):
    # Read line sends data to grep co routine
    child_f = count()
    f = grep(word_to_search, child_f)  # Initialize the grep co routine with the word to search
    for line in read_lines:
        f.send(line)  # Send data to grep co routine


def word_count(file_name, word_to_search):
    # first read file line by line
    with open(file_name) as f:
        read_line(f, word_to_search)


if __name__ == '__main__':
    time = datetime.datetime.now()
    word_count("text_file.txt", "love")
    print("Elapsed", datetime.datetime.now() - time)
