#!/usr/bin/python3
def arg(argv):
    n=len(argv)-1
    if n == 0:
      print("{:d} arguments.".format(n))
    elif n == 1:
      print("{:d} argument:".format(n)
    else:
      print("{:d} arguments:".format(n))

    if n>=1:
      i = 1
        while i <= n:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
      
