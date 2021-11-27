import os
from Supportive import *
from Area import Area
from Tree import Tree


def run_program(kdtree, name):
    print("[{}]: ".format(name), end=""),
    kdtree.print_points(kdtree.points["all"])

    try:
        area_to_find = Area(import_file("input/" + name + "_search"))
    except OSError as e:
        area_to_find = Area((Point(0, 0), Point(0, 0)))
        print(e)

    kdtree.tree.area = Area([Point(0, 0), Point(kdtree.plot_max_size, kdtree.plot_max_size)])
    kdtree.assign_areas(kdtree.tree)
    kdtree.find_solution(kdtree.tree, area_to_find)
    draw_plot(kdtree, area_to_find)
    color_solution(kdtree)
    plt.show()


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            if '_search' not in name:
                f = os.path.join(root, name)
                run_program(Tree(import_file(f), 10), name)


def from_random(points_qty):
    run_program(Tree(generate_random_points(points_qty), 10), "random")


def for_benchmark(points):
    Tree(points, 10)


if __name__ == '__main__':
    from_files()  # uruchamia program z plików z katalogu 'input'
    from_random(20)  # uruchamia z wygenerowanych losowo punktów
