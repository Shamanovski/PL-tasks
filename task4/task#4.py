import sys
import statistics


def main():
    path = sys.argv[1]

    with open(path, "r") as file:
        numbers_array = [int(num) for num in file.readlines()]

    average = statistics.mean(numbers_array)
    average = int(average)  # round up
    ctr = 0
    for number in numbers_array:
        steps = abs(number - average)
        ctr += steps

    print(ctr)


main()
