import os
from SegmentType import SegmentType
from Segment import Segment
from Supportive import import_file, draw_plot, draw_intersections, set_title
from Area import Area
from matplotlib import pyplot as plt
from treelib import Node, Tree


def run_program(area, name):
    draw_plot(area=area)
    tree = Tree()
    sorted_points = area.get_sorted_points()
    print(f"File: {name}")

    iteration = 0
    while sorted_points:
        segment = None
        current_point = sorted_points.pop(0)
        if current_point.is_start:
            segment = current_point.segment

        if current_point.segment_type == SegmentType.HORIZONTAL:
            if iteration == 0:
                tree.create_node(tag=segment, identifier=current_point)
            if current_point.is_start:
                C_Tree.add_node(segment=segment)

            elif not current_point.is_start:
                C_Tree.root = C_Tree.remove_node(root=C_Tree.root, key=(current_point.y, current_point.segment_id))

        elif current_point.segment_type == SegmentType.VERTICAL and current_point.is_start:
            crossed = C_Tree.get_crossed(vertical_segment=segment)

            if crossed:
                v_segment = segment
                for h_segment in crossed:
                    area.add_intersection(segment=h_segment, vertical=v_segment)
                    print(f"Crossing SEGMENT #{h_segment.segment_index}: {h_segment.start}, {h_segment.end}\t\t"
                          f"VERTICAL #{v_segment.segment_index}: {v_segment.start}, {v_segment.end}")

        iteration += 1

    draw_intersections(area=area)
    set_title(area=area, tree=C_Tree)
    print(f"COUNT of crossed segments: {C_Tree.crossed_qty}\n")
    plt.show()


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            points, segments = import_file(f)
            run_program(Area(points=points, segments=segments), name)


if __name__ == '__main__':
    """ 
        It's important to load:
        - VERTICAL segments from BOTTOM to TOP
        - HORIZONTAL segments from LEFT to RIGHT
    """
    from_files()
