import os

from SegmentType import SegmentType
from Segment import Segment
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
        end_of_segment_id = C_Tree.find_end_of_segment(index=current_point.segment_id)
        end_of_segment = C_Tree.points.pop(end_of_segment_id)

        if current_point.segment_type == SegmentType.HORIZONTAL:
            if current_point.is_start:
                segment_id = current_point.segment_id
                C_Tree.tree.append(Segment(start=current_point, end=end_of_segment, segment_index=segment_id))
        elif current_point.segment_type == SegmentType.VERTICAL:
            v_segment = Segment(start=current_point, end=end_of_segment, segment_index=current_point.segment_id)
            crossed = C_Tree.get_crossed(current_point=current_point, vertical_end=end_of_segment)

            if crossed:
                for segment in crossed:
                    area.add_intersection(segment=segment, vertical=v_segment)
                    print(f"Crossing SEGMENT #{segment.segment_index}: {segment.start}, {segment.end}\t\t"
                          f"VERTICAL #{v_segment.segment_index}: {v_segment.start}, {v_segment.end}")

    draw_intersections(area=area)
    set_title(area=area, tree=C_Tree)
    print(f"COUNT of crossed segments: {C_Tree.crossed_qty}\n")
    plt.show()


def from_files():
    for root, dirs, files in os.walk('input/', topdown=False):
        for name in files:
            f = os.path.join(root, name)
            run_program(Area(import_file(f)), name)


if __name__ == '__main__':
    """ 
        It's important to load:
        - VERTICAL segments from TOP to BOTTOM 
        - HORIZONTAL segments from LEFT to RIGHT
    """
    from_files()
