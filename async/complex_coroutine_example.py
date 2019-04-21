import datetime

"""
Make a co routine, which read a file line by line, and find out the word count of a specific word in it
Then main difference in this is that we will search for multiple words count
"""


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


@co_routine
def fan_out(children):
    # For every line we receive, we fan out several child greps
    while True:
        line = yield
        for child in children:
            child.send(line)


def read_line(read_lines, word_to_search_list):
    # Now we multiple word to search in line, so we create multiple grep for every search word
    fan_out_children = []
    for word in word_to_search_list:
        child_f = count()
        fan_out_children.append(grep(word, child_f))

    # Now we call the fan out function, what it does is for every line, it call the multiple word grep
    fan_out_fn = fan_out(fan_out_children)
    for line in read_lines:
        fan_out_fn.send(line)  # Send data to grep co routine 


def word_count(file_name, word_to_search_list):
    # first read file line by line
    with open(file_name) as f:
        read_line(f, word_to_search_list)


if __name__ == '__main__':
    time = datetime.datetime.now()
    word_count("text_file.txt", ["love", "the"])
    print("Elapsed", datetime.datetime.now() - time)
