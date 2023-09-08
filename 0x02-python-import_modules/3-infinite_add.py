#!/usr/bin/python3
import sys

if __name__ == "__main__":

    def inf_add(argv):
        n = len(argv) - 1
        if n == 0:
            print("{:d}".format(n))
            return
        else:
            i = 1
            add = 0
        while i <= n:
            add += int(argv[i])
            i += 1
            print("{:d}".format(add))
    inf_add(sys.argv)
