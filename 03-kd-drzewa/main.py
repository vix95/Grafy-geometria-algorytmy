import os
from Supportive import *
from Area import Area
from Tree import Tree, TreeNode


def run_program(kdtree, name):
    print("[{}]: ".format(name), end=""),
    kdtree.print_points(kdtree.points["all"])
    area_to_find = Area(import_file("input/" + name + "_search"))
    kdtree.tree.area = Area([[0, 0], [kdtree.max_size, kdtree.max_size]])
    assign_areas(kdtree.tree)

    draw_plot(kdtree, area_to_find)
    plt.show()


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            if '_search' not in name:
                f = os.path.join(root, name)
                run_program(Tree(import_file(f), 10), name)


if __name__ == '__main__':
    from_files()  # uruchamia program z plikow z katalogu 'input'
    #from_random(100)  # uruchamia z wygenerowanych losowo punktow