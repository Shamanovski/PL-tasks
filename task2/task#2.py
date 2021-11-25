import sys
import enum
import math


class Distance(enum.Enum):
    OnTheCircle = 0
    InsideTheCircle = 1
    OutsideTheCircle = 2


def main():
    path1, path2 = sys.argv[1], sys.argv[2]
    with open(path1, "r") as file1, open(path2, "r") as file2:
        centre, radius = file1.readlines()
        centre_x, centre_y = centre.split()
        centre_x, centre_y, radius = float(centre_x), float(centre_y), int(radius)
        points = file2.readlines()

    for point in points:
        x, y = point.split()
        x, y = float(x), float(y)
        # comment the formula
        result = math.pow((x - centre_x), 2) + math.pow((y - centre_y), 2) - radius**2
        print(result)
        if result == 0:
            print(Distance.OnTheCircle)
        elif result < 0:
            print(Distance.InsideTheCircle)
        else:
            print(Distance.OutsideTheCircle)


main()
