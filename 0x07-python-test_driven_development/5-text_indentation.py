#!/usr/bin/python3
"""
Module 5-text_indentation
A function that prints a text with 2 new lines
after each of the following characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints text with two new lines after '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    l = [lines.strip(' ') for lines in text.split('\n')]
    rev = "\n".join(l)
    print(rev, end="")
