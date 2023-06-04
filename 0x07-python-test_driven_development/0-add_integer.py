#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Return the integer addition a and b
    Float values are accepted and cast into integers
    Raises:
        TypeError: a must be an integer or b must be an integer
    """
    if type(a) != float and type(a) != int: 
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    
    return (int(a) + int(b))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

