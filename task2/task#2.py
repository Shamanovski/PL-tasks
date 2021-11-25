import sys
import enum
import math


class Distance(enum.IntEnum):
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
        distance_radius_delta = math.pow((x - centre_x), 2) + math.pow((y - centre_y), 2) - radius**2
        if distance_radius_delta == 0:
            print(int(Distance.OnTheCircle))
        elif distance_radius_delta < 0:
            print(int(Distance.InsideTheCircle))
        else:
            print(int(Distance.OutsideTheCircle))


main()
