import os
from Supportive import import_file, draw_plot, draw_circles, plt_setup
from Area import Area
from matplotlib import pyplot as plt


def run_program(area, name):
    draw_plot(area=area)
    print(f"File: {name}")

    area.execute()
    draw_circles(area)
    plt_setup(area)
    plt.show()

    print("------------------")
    print(f"Point Count: {area.point_count}")

    print("X:\t", end="")
    for point in area.raw_point_list:
        print(f"{point.x}", end="  ")

    print("\nY:\t", end="")
    for point in area.raw_point_list:
        print(f"{point.y}", end="  ")

    print(f"\n\nHospital Count: {area.hospital_count}")

    for i, hospital in enumerate(area.hospital_list):
        print(f"Hospital {i + 1}: {hospital}")

    print(f"\n\tr = {area.opt_dist}")


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            point_list = import_file(f)
            run_program(Area(point_list=point_list, hospital_count=3), name)


if __name__ == '__main__':
    from_files()
