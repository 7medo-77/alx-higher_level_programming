#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    i = 1
    signArray = "+-/*"
    res = 0

    if (len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    match sys.argv[2]:
        case "+":
            res = add(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
        case "-":
            res = sub(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
        case "/":
            res = div(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
        case "*":
            res = mul(int(sys.argv[1]), int(sys.argv[3]))
            print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], res))
        case other:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
