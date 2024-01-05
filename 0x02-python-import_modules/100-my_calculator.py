#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    i = 1
    signArray = "+-/*"
    res = 0

    if (len(argv) != 4):
        print(
            "Usage: ./100-my_calculator.py <a> <operator> <b>"
        )
        exit(1)

    match argv[2]:
        case "+":
            res = add(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        case "-":
            sub(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        case "/":
            div(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        case "*":
            mul(int(argv[1]), int(argv[3]))
            print("{} {} {} = {}".format(argv[1], argv[2], argv[3], res))
        case other:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
