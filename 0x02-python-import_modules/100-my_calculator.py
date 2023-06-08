#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as ar
    import calculator_1 as cal

    size = len(ar)
    if (size != 4):
        print("Usage: {} <a> <operator> <b>".format(ar[0]))
        exit(1)
    a = int(ar[1])
    b = int(ar[3])
    sign = ar[2]
    if sign == "+":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, cal.add(a, b)))
    elif sign == "-":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, cal.sub(a, b)))
    elif sign == "*":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, cal.mul(a, b)))
    elif sign == "/":
        print("{:d} {} {:d} = {:d}".format(a, sign, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
