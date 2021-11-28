import sys
from itertools import cycle


def main():
    n, m = int(sys.argv[1]), int(sys.argv[2])
    cycled_array = cycle(range(1, n + 1))
    ctr = 0
    print(1, end="")  # 1-st number
    for number in cycled_array:
        if ctr == m - 1:
            if number == 1 and ctr != 0:  # end of cycle
                return
            print(number, end="")
            ctr = 0
        ctr += 1


main()
