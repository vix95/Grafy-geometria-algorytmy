import os
from SegmentType import SegmentType
from Supportive import import_file, draw_plot, draw_intersections, set_title
from Area import Area
from Tree import Tree
from matplotlib import pyplot as plt


def run_program(area, name):
    draw_plot(area=area)
    C_Tree = Tree()
    C_Tree.points = area.get_sorted_points()
    print(f"File: {name}")

    while C_Tree.points:
        current_point = C_Tree.points.pop(0)
        if current_point.segment.segment_type == SegmentType.HORIZONTAL:
            if current_point.is_start:
                C_Tree.root = C_Tree.insert_node(segment=current_point.segment, root=C_Tree.root, key=current_point.segment.start.y)

            elif not current_point.is_start:
                C_Tree.root = C_Tree.delete_node(root=C_Tree.root, key=current_point.y)

        elif current_point.segment.segment_type == SegmentType.VERTICAL and current_point.is_start:
            crossed = C_Tree.get_crossed(vertical_segment=current_point.segment)

            if crossed:
                v_segment = current_point.segment
                for h_segment in crossed:
                    area.add_intersection(segment=h_segment, vertical=v_segment)
                    print(f"Crossing SEGMENT #{h_segment.segment_index}: {h_segment.start}, {h_segment.end}\t\tVERTICAL #{v_segment.segment_index}: {v_segment.start}, {v_segment.end}")

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
