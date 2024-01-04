#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    arg = "argument" if len(sys.argv) == 2 else "arguments"
    sep = ":" if len(sys.argv) > 1 else "."

    print("{} {}{}".format(len(sys.argv) - 1, arg, sep))
    while (i < len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
