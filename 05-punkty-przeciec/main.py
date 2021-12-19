import os
from Supportive import import_file, draw_plot, draw_line, draw_intersections
from Area import Area
from matplotlib import pyplot as plt


def find_intersection( p0, p1, p2, p3 ) :
    s10_x = p1[0] - p0[0]
    s10_y = p1[1] - p0[1]
    s32_x = p3[0] - p2[0]
    s32_y = p3[1] - p2[1]
    denom = s10_x * s32_y - s32_x * s10_y

    if denom == 0 : return None # collinear

    denom_is_positive = denom > 0
    s02_x = p0[0] - p2[0]
    s02_y = p0[1] - p2[1]
    s_numer = s10_x * s02_y - s10_y * s02_x

    if (s_numer < 0) == denom_is_positive : return None # no collision
    t_numer = s32_x * s02_y - s32_y * s02_x
    if (t_numer < 0) == denom_is_positive : return None # no collision
    if (s_numer > denom) == denom_is_positive or (t_numer > denom) == denom_is_positive : return None # no collision

    # collision detected
    t = t_numer / denom

    intersection_point = [ p0[0] + (t * s10_x), p0[1] + (t * s10_y) ]
    return intersection_point


def run_program(area, name):
    draw_plot(area)
    draw_line(area)

    line_segments = area.points
    intersections = set()
    for i in range(0, 15):
        test_segment = [(i, 0), (i, 15)]
        area.line = i
        for line_segment in line_segments:
            if area.met_horizontal_line(line_segment):
                p0, p1 = test_segment[0], test_segment[1]
                p2, p3 = line_segment[0], line_segment[1]
                result = find_intersection(p0, p1, p2, p3)
                if result is not None:
                    intersections.add(tuple(result))
                    area.add_intersection(result)

    draw_intersections(area)
    area.print_intersections()
    plt.show()


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            run_program(Area(import_file(f)), name)


if __name__ == '__main__':
    from_files()

