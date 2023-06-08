#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4 as hid
    ar = dir(hid)
    for name in ar:
        if name[:2] != '__':
            print("{}".format(name))
