import os
from Supportive import *
from Area import *


def run_program(area, name):
    if len(area.points.get("all")) > 3:
        print("[{}] S:".format(name)),
        area.print_points(area.points["all"])

        draw_plot(area)
        draw_line(area)
        draw_points_connection(area)
        show_results(area)

        plt.show()


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            run_program(Area(import_file(f)), name)


def from_random(points_qty):
    run_program(Area(generate_random_points(points_qty)), "random")


def for_benchmark(points):
    Area(points)


if __name__ == '__main__':
    from_files()  # uruchamia program z plikow z katalogu 'input'
    from_random(20)  # uruchamia z wygenerowanych losowo punktow
