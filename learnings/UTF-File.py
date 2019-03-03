from functools import partial
from codecs import iterdecode


# Returns an iterator of unicode chunks from the given path.
import magic


def iter_unicode_chunks(path, encoding):
    # Open the input file.
    with open(path, "rb") as input:
        # Convert the binary file into binary chunks.
        binary_chunks = iter(partial(input.read, 1), "")
        # Convert the binary chunks into unicode chunks.
        for unicode_chunk in iterdecode(binary_chunks, encoding):
            yield unicode_chunk


from codecs import iterencode


# Writes an iterator of unicode chunks to the given path.
def write_unicode_chunks(path, unicode_chunks, encoding):
    # Open the output file.
    with open(path, "wb") as output:
        # Convert the unicode chunks to binary.
        for binary_chunk in iterencode(unicode_chunks, encoding):
            output.write(binary_chunk)


def read_and_write_as_utf8(file_path, html_file_path):
    """
    Open a file and write as UTF8.
    :param file_path: The actual file path
    :param html_file_path: The new file path name
    :return: None
    """
    input = open(file_path, "rb")
    output = open(html_file_path, "w", encoding="utf-8")

    # Stream chunks of unicode data.
    with input, output:
        while True:
            # Read a chunk of data.
            chunk = input.read(4096)
            print("Chunk", chunk)
            if not chunk:
                break
            output.write(str(chunk))


def get_probable_encoding(file_path):
    with open(file_path, 'rb') as f:
        blob = f.read()
        m = magic.Magic(mime_encoding=True)
        return m.from_buffer(blob)
