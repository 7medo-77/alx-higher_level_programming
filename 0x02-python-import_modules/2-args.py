#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    arg = "argument" if len(argv) == 2 else "arguments"
    sep = ":" if len(argv) > 1 else "."

    print("{} {}{}".format(len(argv) - 1, arg, sep))
    while (i < len(argv)):
        print("{}: {}".format(i, argv[i]))
        i += 1
