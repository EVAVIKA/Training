def less_that_5(number, p):
    if number < 5:
        p(number)


def increment(step=1):
    return lambda x: x + step  # x: x + 3


if __name__ == '__main__':
    inc = increment(1)
    less_that_5(inc(4), lambda number: print(str(number) + " < 5"))
