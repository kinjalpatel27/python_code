import numpy as np


def find_height(boxes, idx=0, prev_box=None):
    if idx >= len(boxes):
        return 0

    height_with = 0

    if prev_box is not None:
        if (
            boxes[idx][0] < prev_box[0]
            and boxes[idx][1] < prev_box[1]
            and boxes[idx][2] < prev_box[2]
        ):
            height_with = boxes[idx][1]
            height_with += find_height(boxes, idx + 1, boxes[idx])
    else:
        height_with = boxes[idx][1]
        height_with += find_height(boxes, idx + 1, boxes[idx])
    height_without = find_height(boxes, idx + 1, prev_box)

    return max(height_with, height_without)


def stack_height(boxes):
    sort_boxes = sorted(boxes, key=lambda x: x[1], reverse=True)
    print(sort_boxes)
    print(find_height(boxes))


n = 8
boxes = np.random.randint(1, 25, (n, 3))
print(boxes)
stack_height(boxes)
