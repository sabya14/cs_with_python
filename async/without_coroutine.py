import datetime

n = 0


def grep(text, substring):
    count(text.count(substring))


def count(value):
    global n
    n += value


def read_line(read_lines, word_to_search):
    # Read line sends data to grep co routine
    for line in read_lines:
        grep(line, word_to_search)


def word_count(file_name, word_to_search):
    # first read file line by line
    with open(file_name) as f:
        read_line(f, word_to_search)
    print("Sustring", word_to_search, n)


if __name__ == '__main__':
    time = datetime.datetime.now()
    word_count("text_file.txt", "love")
    print("Elapsed", datetime.datetime.now() - time)
