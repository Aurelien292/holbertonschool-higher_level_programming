#!/usr/bin/python3
"""
    Writes a string to a text file (UTF-8 encoded) and returns the number of
    characters written.
    """


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8 encoded) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file where the string will be written.
        If the file does not exist, it will be created.
                         If it exists, its contents will be overwritten.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If the file cannot be opened for writing or any
        I/O operation fails.

    Example:
        write_file("example.txt", "Hello, world!")
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
