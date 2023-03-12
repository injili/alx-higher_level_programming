#!/usr/bin/python3

if __name__ == "__main__":
    """print out names from within a compiled module"""
    import hidden_4

    names = dir(hiddden_4)
    for name in names:
        for name in names:
            if name[:2] != "__":
                print(name)
