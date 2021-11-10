import os
from Supportive import *
from Point import Polygon

if __name__ == '__main__':
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            polygon = Polygon(import_file(f), name)
            check_orientation(polygon)  # checking on first 3 points
            find_min_and_max(polygon)
            is_kernel(polygon)
            draw_plot(polygon)
            if polygon.is_kernel:
                draw_min_max(polygon)
                if polygon.two_points_at_least():
                    draw_perimeter(polygon)
            set_title(polygon)
            plt.show()
