#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.1f}".format(result))
    except ZeroDivisionError:
        result = None
        print("Division by zero! Inside result: {}".format(result))
    except Exception as e:
        result = None
        print("An error occurred: {}. Inside result: {}".format(e, result))
    finally:
        return result

