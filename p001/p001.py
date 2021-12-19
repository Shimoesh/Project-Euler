# Solution to Project Euler problem 1
# Copyright (c) Jitan Vaghela. All rights reserved.
#
# https://jitan.co.uk/project-euler-solutions
# https://github.com/Shimoesh/Project-Euler
#
# Problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

DEBUG = False


def p001(limit):
    result = 0
    for i in range(limit):
        if (i % 3 == 0) or (i % 5 == 0):
            if DEBUG:
                print(f"Number found {i}")
            result += i
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # p001(10)
    p001(1000)