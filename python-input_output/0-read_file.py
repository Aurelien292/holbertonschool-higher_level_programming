#!/usr/bin/python3

"""
    Reads the content of a text file (UTF-8 encoded) and prints it
    to standard output.
    """


def read_file(filename=""):
    """
    Reads the content of a text file (UTF-8 encoded) and prints it
    to standard output.

    Args:
        filename (str): The name of the file to read. Defaults to
        an empty string,
                         which will not work as expected. Provide
                         a valid file path.

    Returns:
        None: This function does not return any value. It only
        prints the content of
              the file to the standard output.

    Raises:
        FileNotFoundError: If the specified file does not exist or
        cannot be found.
        IOError: If the file cannot be opened or read for any other reason.

    Example:
        read_file("example.txt")
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
