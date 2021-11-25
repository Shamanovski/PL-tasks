import sys
from itertools import cycle


def main():
    result = []
    n, steps = int(sys.argv[1]), int(sys.argv[2])
    cycled_array = cycle(range(1, n + 1))
    ctr = 0
    digit = 0
    while True:
        ctr += 1
        digit = next(cycled_array)
        if ctr == steps:
            if digit == 1:  # if the end of the cycled array
                print(result)
                return
            result.append(digit)
            ctr = 0


main()
