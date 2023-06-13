#!/usr/bin/python3
"""
module 100-append_after
A function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts line after a specific string file

    Args:
        filename: name of the file to mod
        search_string: string to be found
        new_string: string to be appended
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, mode="w", encoding="utf-8") as f:
        new_text = ""
        for line in lines:
            f.write(line)
            if search_string in line:
                line.write("\n" + new_string + "\n")
        f.seek(0)
        f.write(new_text)
